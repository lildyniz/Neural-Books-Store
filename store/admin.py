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
    prepopulated_fields = {'slug': ('name',)}
    
    list_display = ['name', 'slug', 'price', 'discount', 
                    'total_price', 'available',
                    'written', 'created', 'image']
    list_editable = ['price', 'discount', 'available']
    list_filter = ['price', 'discount', 'available', 'created']
    search_fields = ['name', 'description']