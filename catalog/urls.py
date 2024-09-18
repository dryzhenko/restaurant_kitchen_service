from django.urls import path

from catalog.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishDetailView,
    DishTypeListView,
    DishTypeDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish/type/", DishTypeListView.as_view(), name="dish_type-list"),
    path("dish/type/<int:pk>", DishTypeDetailView.as_view(), name="dish_type-detail"),
    path("dish/type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish/type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish/type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]

app_name = "catalog"
