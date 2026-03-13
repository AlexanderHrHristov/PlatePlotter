from django.contrib import admin
from .models import Product, Store, Inventory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'store', 'category', 'unit', 'price', 'is_basic')