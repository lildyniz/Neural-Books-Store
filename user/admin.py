from django.contrib import admin

from .models import User
from cart.admin import CartTabAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']

    inlines = [CartTabAdmin,]