from django.urls import path

from .views import (
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    RecipeItemCreateView,
    RecipeItemUpdateView,
    RecipeItemDeleteView,
)

urlpatterns = [
    path('dishes/', DishListView.as_view(), name='dish-list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('dishes/create/', DishCreateView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/edit/', DishUpdateView.as_view(), name='dish-edit'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish-delete'),

    path('recipe-items/create/', RecipeItemCreateView.as_view(), name='recipeitem-create'),
    path('recipe-items/<int:pk>/edit/', RecipeItemUpdateView.as_view(), name='recipeitem-edit'),
    path('recipe-items/<int:pk>/delete/', RecipeItemDeleteView.as_view(), name='recipeitem-delete'),
]