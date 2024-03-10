from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Author, Book
from .utils import q_search
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from django.db.models import Q


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

    with_discount = request.GET.get('with_discount', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    page = request.GET.get('page', 1)

    category = None
    author = None
    
    if slug == 'all':
        books = Book.objects.filter(available=True)
    elif query:
        books = q_search(query)
    else:
        try:
            category = get_object_or_404(Category, slug=slug)
            books = Book.objects.filter(category=category, available=True)
        except:
            author = get_object_or_404(Author, slug=slug)
            books = Book.objects.filter(author=author, available=True)

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

    author_ids = book.author.values_list("id", flat=True)
    category_ids = book.category.values_list("id", flat=True)

    # similar_books = Book.objects.filter(
    #     Q(author__id__in=author_ids) | Q(category__id__in=category_ids)
    #     ).exclude(pk=book.pk).prefetch_related('author', 'category').order_by('pk')[:5]

    from django.db.models import Count

    similar_books = Book.objects.filter(
        Q(author__id__in=author_ids) | Q(category__id__in=category_ids)
        ).exclude(pk=book.pk).annotate(
        match_count=Count(
            'author',
            filter=Q(author__id__in=author_ids),
        )
        + Count(
            'category',
            filter=Q(category__id__in=category_ids),
        )).order_by('-match_count')[:5]

    
    return render(
        request,
        "store/book/detail.html",
        {
            "book": book,
            "cart_product_form": cart_product_form,
            "similar_books": similar_books
        },
    )
