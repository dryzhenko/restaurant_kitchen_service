from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Dish, Cook, Ingredients, DishType


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Appetizer")

    def test_dish_type_unique(self):
        with self.assertRaises(Exception):
            DishType.objects.create(name="Appetizer")  # Duplicate should raise an error


class CookModelTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="supersecret",
            years_of_experience=5,
        )

    def test_cook_creation(self):
        self.assertEqual(self.cook.username, "testcook")
        self.assertEqual(self.cook.years_of_experience, 5)

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "testcook")


class IngredientsModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredients.objects.create(name="Tomato")

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "Tomato")

    def test_ingredient_unique(self):
        with self.assertRaises(Exception):
            Ingredients.objects.create(name="Tomato")  # Duplicate should raise an error


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="supersecret",
            years_of_experience=3,
        )
        self.ingredient = Ingredients.objects.create(name="Cheese")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Delicious cheese pizza",
            price=9.99,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_creation(self):
        self.assertEqual(self.dish.name, "Pizza")
        self.assertEqual(self.dish.description, "Delicious cheese pizza")
        self.assertEqual(self.dish.price, 9.99)
        self.assertEqual(self.dish.dish_type, self.dish_type)

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Pizza")

    def test_dish_has_cooks(self):
        self.assertIn(self.cook, self.dish.cooks.all())

    def test_dish_has_ingredients(self):
        self.assertIn(self.ingredient, self.dish.ingredients.all())
