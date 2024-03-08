from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:book_list", args=[self.slug])


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)  
    country = models.CharField(max_length=100)
    birth = models.DateField()
    image = models.ImageField(upload_to="authors/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["birth"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:book_list", args=[self.slug])


class Book(models.Model):
    category = models.ManyToManyField(Category, related_name="books", verbose_name='Категория')
    author = models.ManyToManyField(Author, related_name="author_books", verbose_name='Автор')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    image = models.ImageField(upload_to="books/%Y/%m/%d", blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='Доступный')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    written = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2024)], verbose_name='Написана')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='Скидка')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена со скидкой')

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
            models.Index(fields=["-written"]),
        ]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total_price = round(self.price - self.price*self.discount/100, 2)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("store:book_detail", args=[self.id, self.slug])

    def display_id(self):
        return f'{self.id:05}'