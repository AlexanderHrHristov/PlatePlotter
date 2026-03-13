from django.contrib import admin
from .models import Dish, RecipeItem


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeItemInline]


@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    list_display = ('dish', 'product', 'quantity_needed')
    list_filter = ('dish',)
    search_fields = ('dish__name', 'product__name', 'product__brand')
