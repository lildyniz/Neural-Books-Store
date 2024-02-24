from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Book
from cart.forms import CartAddProductForm


def index(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    books = Book.objects.filter(available=True)

    return render(request,
                  'store/book/index.html',
                  {'categories': categories,
                   'authors': authors,
                   'books': books})


def book_list(request, slug=None):
    category = None
    categories = Category.objects.all()
    author = None
    authors = Author.objects.all()
    books = Book.objects.filter(available=True)

    if slug:
        try:
            category = get_object_or_404(Category,
                                         slug=slug)
            books = books.filter(category=category)
        except:
            author = get_object_or_404(Author,
                                       slug=slug)
            books = books.filter(author=author)

    return render(request,
                  'store/book/list.html',
                  {'category': category,
                   'categories': categories,
                   'author': author,
                   'authors': authors,
                   'books': books})


def book_detail(request, id, slug):
    book = get_object_or_404(Book,
                             id=id,
                             slug=slug,
                             available=True)
    categories = Category.objects.all()
    authors = Author.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request,
                  'store/book/detail.html',
                  {'book': book,
                   'categories': categories,
                   'authors': authors,
                   'cart_product_form': cart_product_form})