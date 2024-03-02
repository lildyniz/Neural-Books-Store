from decimal import Decimal
from django.conf import settings
from store.models import Book

class Cart:
    def __init__(self, request):
        """Инициализировать корзину"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохранить пустую корзину в сеансе.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book, quantity=1, override_quantity=False):
        """Добавить товар в корзину, либо обновить его количество."""
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0,
                                     'price': str(book.price)}
        if override_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def remove(self, book):
        """Удалить товар из корзины."""
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def save(self):
        # Пометить сеанс как "измененный", что бы обеспечить его сохранение.
        self.session.modified = True

    def __iter__(self):
        """Прокрутить товарные позиции в корзине в цикле и
        полчить товары из базы данных."""
        book_ids = self.cart.keys()
        # Получить объекты book и добавить их в корзину.
        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """Подсчитать все товарные позиции в корзине."""
        return sum(item['quantity'] for item in self.cart.values())
    
    def total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # Удалить корзину из сеанса.
        del self.session[settings.CART_SESSION_ID]
        self.save()