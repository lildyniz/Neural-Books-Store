from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string


# from .cart import Cart
from .models import Cart
from .forms import CartAddProductForm
from .utils import get_user_carts

# @require_POST
# def cart_add(request, book_id):
#     cart = Cart(request)
#     book = get_object_or_404(Book, id=book_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(book=book,
#                  quantity=cd['quantity'],
#                  override_quantity=cd['override'])
#     return redirect('cart:cart_detail')

# @require_POST
# def cart_remove(request, book_id):
#     cart = Cart(request)
#     book = get_object_or_404(Book, id=book_id)
#     cart.remove(book)
#     return redirect('cart:cart_detail')

# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
#                                                                    'override': True})
#     return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request):

    product_id = request.POST.get("product_id")
    product = Book.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity = 1)
    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html
    }

    return JsonResponse(response_data)

    return 

def cart_change(request, book_slug):
    ...

def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])