from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Dish, DishType, Cook, Ingredients


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_cookers": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
    }

    return render(request, "catalog/index.html", context=context)


class CookListView(ListView):
    model = Cook
    queryset = Cook.objects.all().order_by('first_name')
    paginate_by = 5
    template_name = "catalog/cook_list.html"
    context_object_name = "cook_list"


class CookDetailView(DetailView):
    model = Cook
    template_name = "catalog/cook_details.html"
    context_object_name = "cook_detail"


class DishListView(ListView):
    model = Dish
    queryset = Dish.objects.all().order_by('name')
    paginate_by = 5
    template_name = "catalog/dish_list.html"
    context_object_name = "dish_list"


class DishDetailView(DetailView):
    model = Dish
    template_name = "catalog/dish_detail.html"
    context_object_name = "dish_detail"


class DishTypeListView(ListView):
    model = DishType
    queryset = DishType.objects.all().order_by('name')
    paginate_by = 5
    template_name = "catalog/dish_type.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = "catalog/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class IngredientListView(ListView):
    model = Ingredients
    queryset = Ingredients.objects.all().order_by('name')
    paginate_by = 5
    template_name = "catalog/ingredients_list.html"
    context_object_name = "ingredient_list"
