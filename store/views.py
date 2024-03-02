from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Author, Book
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def index(request):
    books = Book.objects.filter(available=True)

    rec_books = books.order_by('-written')[:18]
    new_books = books.order_by('written')[:18]
    best_books = books.order_by('created')[:18]

    return render(request,
                  "store/book/index.html",
                  {"books": books, 'rec_books': rec_books,
                   'new_books': new_books, 'best_books': best_books},)


def book_list(request, slug):

    with_discount = request.GET.get('with_discount', None)
    order_by = request.GET.get('order_by', None)

    page = request.GET.get('page', 1)

    category = None
    author = None
    books = Book.objects.filter(available=True)

    if slug != 'all':
        try:
            category = get_object_or_404(Category, slug=slug)
            books = get_list_or_404(books.filter(category=category))
        except:
            author = get_object_or_404(Author, slug=slug)
            books = get_list_or_404(books.filter(author=author))
            # Надо добавить проверку get_list_or_404(), что бы в случае 
            # отсутствия у автора/категории книг выводилась страница "Упс. Ничего нет".

    if with_discount:
        books = books.filter(discount__gt=0).order_by('-discount')
    if order_by and order_by != 'default':
        books = books.order_by(order_by)

    paginator = Paginator(books, 12)
    current_page = paginator.page(page)

    return render(
        request,
        "store/book/list.html",
        {
            "category": category,
            "author": author,
            "books": current_page,
            'slug_url': slug
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
