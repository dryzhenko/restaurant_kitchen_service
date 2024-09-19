from django.test import TestCase
from catalog.forms import (
    CookCreationForm,
    CookExperienceUpdateForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm
)


class CookCreationFormTest(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "newcook",
            "password1": "supersecretpassword",
            "password2": "supersecretpassword",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_creation_form_invalid(self):
        form_data = {
            "username": "newcook",
            "password1": "supersecretpassword",
            "password2": "supersecretpassword",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class CookExperienceUpdateFormTest(TestCase):
    def test_experience_update_form_invalid_large_experience(self):
        form_data = {"years_of_experience": 123}  # Over 2 digits
        form = CookExperienceUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_experience_update_form_negative_experience(self):
        form_data = {"years_of_experience": -5}
        form = CookExperienceUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_experience_update_form_non_digit_experience(self):
        form_data = {"years_of_experience": "ten"}
        form = CookExperienceUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())


class CookSearchFormTest(TestCase):
    def test_cook_search_form_empty(self):
        form = CookSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_cook_search_form_with_username(self):
        form = CookSearchForm(data={"username": "someuser"})
        self.assertTrue(form.is_valid())


class DishSearchFormTest(TestCase):
    def test_dish_search_form_empty(self):
        form = DishSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_dish_search_form_with_name(self):
        form = DishSearchForm(data={"name": "Pizza"})
        self.assertTrue(form.is_valid())


class DishTypeSearchFormTest(TestCase):
    def test_dish_type_search_form_empty(self):
        form = DishTypeSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_with_name(self):
        form = DishTypeSearchForm(data={"name": "Appetizer"})
        self.assertTrue(form.is_valid())
