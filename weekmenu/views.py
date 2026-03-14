from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import WeekMenuForm, MealForm, MealEditForm
from .models import WeekMenu, Meal


class WeekMenuListView(ListView):
    model = WeekMenu
    template_name = "weekmenu/weekmenu-list.html"
    context_object_name = "weekmenus"


class WeekMenuDetailView(DetailView):
    model = WeekMenu
    template_name = "weekmenu/weekmenu-detail.html"
    context_object_name = "weekmenu"


class WeekMenuCreateView(CreateView):
    model = WeekMenu
    form_class = WeekMenuForm
    template_name = "weekmenu/weekmenu-create.html"
    success_url = reverse_lazy("weekmenu-list")


class WeekMenuUpdateView(UpdateView):
    model = WeekMenu
    form_class = WeekMenuForm
    template_name = "weekmenu/weekmenu-edit.html"
    success_url = reverse_lazy("weekmenu-list")


class WeekMenuDeleteView(DeleteView):
    model = WeekMenu
    template_name = "weekmenu/weekmenu-delete.html"
    success_url = reverse_lazy("weekmenu-list")


class MealCreateView(CreateView):
    model = Meal
    form_class = MealForm
    template_name = "weekmenu/meal-create.html"
    success_url = reverse_lazy("weekmenu-list")


class MealUpdateView(UpdateView):
    model = Meal
    form_class = MealEditForm
    template_name = "weekmenu/meal-edit.html"
    success_url = reverse_lazy("weekmenu-list")


class MealDeleteView(DeleteView):
    model = Meal
    template_name = "weekmenu/meal-delete.html"
    success_url = reverse_lazy("weekmenu-list")

# Create your views here.
