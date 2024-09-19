from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if len(years_of_experience) > 2:
            raise ValidationError(
                "You have entered a number that is too large for years of experience."
            )
        if years_of_experience < 0:
            raise ValidationError(
                "Years of experience must be greater than 0."
            )
        if years_of_experience.isalpha():
            raise ValidationError(
                "Years of experience must be a digit."
            )


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"
        widgets = {
            'cooks': forms.CheckboxSelectMultiple(),
            'ingredients': forms.CheckboxSelectMultiple(),
        }


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username",
            }
        )
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by dish name",
            }
        )
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by dish type name",
            }
        )
    )
