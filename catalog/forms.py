from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Cook, Ingredients


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_ofExperience",)

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
