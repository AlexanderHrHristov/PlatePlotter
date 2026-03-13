from django.contrib import admin
from .models import Product, Store, Inventory

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'store', 'unit', 'price', 'is_basic')
    list_filter = ('store', 'unit', 'is_basic')
    search_fields = ('name', 'brand')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'available_quantity', 'minimum_quantity')
    search_fields = ('product__name', 'product__brand')