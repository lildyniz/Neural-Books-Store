from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
# from .cart import Cart
from .models import Cart
from .forms import CartAddProductForm

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

def cart_add(request, book_slug):
    product = Book.objects.get(slug=book_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity = 1)
    
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, book_id):
    ...

def cart_remove(request, book_id):
    ...