from django.urls import path

from catalog.views import index, CookListView, CookDetailView, DishListView, DishDetailView, DishTypeListView, DishTypeDetailView, IngredientListView

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dish/type/", DishTypeListView.as_view(), name="dish_type-list"),
    path("dish/type/<int:pk>", DishTypeDetailView.as_view(), name="dish_type-detail"),
    path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
]

app_name = "catalog"
