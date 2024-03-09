from django.shortcuts import render, redirect
from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateOrderForm
from .models import Order, OrderItem
from cart.models import Cart

@login_required
def create_order(request):

    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    total_amount_order = cart_items.total_price_cart()
                    
                    # Create order.
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            total_amount_order=total_amount_order,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Create ordered items
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.total_price
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                      В наличии - {product.quantity}')
                            
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Clean cart after creating an order
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('user:cart')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)


    return render(request, 'order/create_order.html', {'form': form, 'order': True},)