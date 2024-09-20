from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import (
    CookCreationForm,
    CookExperienceUpdateForm,
    DishForm, DishSearchForm,
    CookSearchForm,
    DishTypeSearchForm
)
from catalog.models import (
    Dish,
    DishType,
    Cook,
    Ingredients
)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_cookers": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    queryset = Cook.objects.all().order_by("first_name")
    paginate_by = 5
    template_name = "catalog/cook_list.html"
    context_object_name = "cook_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        context["search_form"] = CookSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return self.queryset.filter(username__icontains=username)
        return self.queryset


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "catalog/cook_detail.html"
    context_object_name = "cook_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredients.objects.filter(
            dishes__cooks=self.object
        ).distinct()
        return context


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("catalog:cook-list")
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("catalog:cook-list")
    form_class = CookExperienceUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("catalog:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.all().order_by("name")
    paginate_by = 5
    template_name = "catalog/dish_list.html"
    context_object_name = "dish_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["search_form"] = DishSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "catalog/dish_detail.html"
    context_object_name = "dish_detail"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish-list")
    template_name = "catalog/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish-list")
    template_name = "catalog/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("catalog:dish-list")
    template_name = "catalog/dish_confirm_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    queryset = DishType.objects.all().order_by("name")
    paginate_by = 5
    template_name = "catalog/dish_type_list.html"
    context_object_name = "dish_type_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["search_form"] = DishTypeSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "catalog/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish_type-list")
    template_name = "catalog/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("catalog:dish_type-list")
    template_name = "catalog/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("catalog:dish_type-list")
    template_name = "catalog/dish_type_confirm_delete.html"
    context_object_name = "dish_type"
