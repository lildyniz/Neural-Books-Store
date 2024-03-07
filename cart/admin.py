from django.contrib import admin
from . models import Cart

class CartTabAdmin(admin.TabularInline):

    model = Cart
    
    list_display = 'user', 'product', 'quantity', 'session_key', 'created_timestamp'
    search_fields = 'user', 'session_key', 'product', 'created_timestamp'
    readonly_fields = ("created_timestamp",)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    
    list_display = ['user_display', 'product', 'quantity', 
                    'session_key', 'created_timestamp']
    list_editable = ['product', 'quantity']
    search_fields = ['user_display', 'session_key', 'product', 'created_timestamp']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
