from django.db import models
from store.models import Book
from user.models import User

class CartQueryset(models.QuerySet):
    
    def total_price_cart(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity_cart(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQueryset().as_manager()

    def product_price(self):
        return round(self.product.total_price * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Кол-во {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Кол-во {self.quantity}'