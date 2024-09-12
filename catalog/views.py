from django.shortcuts import render
from catalog.models import Dish, DishType, Cook


def index(request):
    num_cookers = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    data = {
        "num_cookers": num_cookers,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "catalog/index.html", context=data)
