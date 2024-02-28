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
        return reverse("store:book_list_by_category", args=[self.slug])


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
        return reverse("store:book_list_by_category", args=[self.slug])


class Book(models.Model):
    category = models.ManyToManyField(Category, related_name="books")
    author = models.ManyToManyField(Author, related_name="author_books")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to="books/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    available = models.BooleanField(default=True)
    written = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2024)])
    created = models.DateTimeField(auto_now_add=True)

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

    def get_absolute_url(self):
        return reverse("store:book_detail", args=[self.id, self.slug])

    def display_id(self):
        return f'{self.id:05}'
    
    def discounted_price(self):
        return round(self.price - self.price*self.discount/100, 2)