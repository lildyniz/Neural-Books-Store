from django.contrib import admin
from .models import Category, Author, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country', 'birth', ]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available',
                    'written', 'created']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']