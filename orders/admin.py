from django.contrib import admin

from .models import Order, OrderItem


class OrderItemTabAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = ("product", "name",)
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = ("order", "product", "name",)


class OrderTabAdmin(admin.TabularInline):
    model = Order
    fields = "requires_delivery", "status", "payment_on_get", "is_paid", "created"
    search_fields = ("requires_delivery", "payment_on_get", "is_paid", "created",)
    readonly_fields = ("created",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "id", "user", "requires_delivery", "status", "payment_on_get", "is_paid", "created"
    search_fields = ("id", "is_paid", "user",)
    readonly_fields = ("created",)
    list_filter = ("is_paid", "status",)
    inlines = (OrderItemTabAdmin,)