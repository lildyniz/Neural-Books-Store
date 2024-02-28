from django.shortcuts import render, get_object_or_404
from .models import Category, Author, Book
from cart.forms import CartAddProductForm


def index(request):
    books = Book.objects.filter(available=True)

    rec_books = books.order_by('-written')[:18]
    new_books = books.order_by('written')[:18]
    best_books = books.order_by('created')[:18]

    return render(request,
                  "store/book/index.html",
                  {"books": books, 'rec_books': rec_books,
                   'new_books': new_books, 'best_books': best_books},)


def book_list(request, slug=None):
    category = None
    author = None
    books = Book.objects.filter(available=True)

    if slug:
        try:
            category = get_object_or_404(Category, slug=slug)
            books = books.filter(category=category)
        except:
            author = get_object_or_404(Author, slug=slug)
            books = books.filter(author=author)

    return render(
        request,
        "store/book/list.html",
        {
            "category": category,
            "author": author,
            "books": books,
        },
    )


def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "store/book/detail.html",
        {
            "book": book,
            "cart_product_form": cart_product_form,
        },
    )
