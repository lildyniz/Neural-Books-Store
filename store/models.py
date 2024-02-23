from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:book_list_by_category',
                       args=[self.slug])
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    country = models.CharField(max_length=100)
    birth = models.DateField()
    image = models.ImageField(upload_to='authors/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['birth']),
            ]
        verbose_name = 'author'
        verbose_name_plural = 'authors'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:book_list_by_category',
                       args=[self.slug])
    
class Book(models.Model):
    category = models.ManyToManyField(Category,
                                      related_name='books')
    author = models.ManyToManyField(Author,
                                   related_name='author_books')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='books/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    written = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
            models.Index(fields=['-written']),
            ]
        verbose_name = 'book'
        verbose_name_plural = 'books'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:book_detail',
                       args=[self.id, self.slug])