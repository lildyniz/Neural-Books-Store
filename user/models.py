from django.db import models
from django.contrib.auth.models import AbstractUser

from store.models import Book


class User(AbstractUser):
    image = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
    favorite_products = models.ManyToManyField(Book, related_name="users_who_favorited", verbose_name='Избранное')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username
