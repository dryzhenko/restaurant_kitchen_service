from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import Cook, Dish, DishType, Ingredients


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info:", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info:", {"fields": ("years_of_experience",)}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price",)
    search_fields = ("name",)
    list_filter = ("dish_type",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "unit",)
    search_fields = ("name",)
