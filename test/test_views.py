from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from catalog.models import Cook, Dish, DishType, Ingredients


class CookListViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")

    def test_cook_list_search(self):
        response = self.client.get(
            reverse("catalog:cook-list") + "?username=testcook"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testcook")


class CookDetailViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword", years_of_experience=5
        )
        self.client.login(username="testcook", password="testpassword")

    def test_cook_detail_view(self):
        response = self.client.get(
            reverse("catalog:cook-detail", args=[self.cook.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook.username)


class CookCreateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")

    def test_cook_create_view(self):
        form_data = {
            "username": "newcook",
            "password1": "supersecretpassword",
            "password2": "supersecretpassword",
            "years_of_experience": 5,
        }
        response = self.client.post(
            reverse("catalog:cook-create"), data=form_data
        )
        self.assertEqual(response.status_code, 302)


class DishListViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Test pizza",
            price=10.00,
            dish_type=self.dish_type
        )

    def test_dish_list_view(self):
        response = self.client.get(reverse("catalog:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")

    def test_dish_list_search(self):
        response = self.client.get(
            reverse("catalog:dish-list") + "?name=Pizza"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")


class DishDetailViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Test pizza",
            price=10.00,
            dish_type=self.dish_type
        )

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse(
                "catalog:dish-detail",
                args=[self.dish.id]
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")


class DishCreateViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_dish_create_view(self):
        DishType.objects.get_or_create(name="Main Course")
        form_data = {
            "name": "Test Dish",
            "description": "Test description",
            "price": 20.00,
            "dish_type": DishType.objects.get(name="Main Course").id,
            "cooks": [],
            "ingredients": []
        }
        response = self.client.post(
            reverse("catalog:dish-create"),
            data=form_data
        )
        self.assertEqual(response.status_code, 200)


class DishUpdateViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Test pizza",
            price=10.00,
            dish_type=self.dish_type
        )

    def test_dish_update_view(self):
        form_data = {
            "name": "Updated Pizza",
            "description": "Updated description",
            "price": 12.00,
            "dish_type": self.dish_type.id,
        }
        response = self.client.post(
            reverse(
                "catalog:dish-update",
                args=[self.dish.id]
            ),
            data=form_data
        )
        self.assertEqual(response.status_code, 200)
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Pizza")


class DishDeleteViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook", password="testpassword"
        )
        self.client.login(username="testcook", password="testpassword")
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Pizza",
            description="Test pizza",
            price=10.00,
            dish_type=self.dish_type
        )

    def test_dish_delete_view(self):
        response = self.client.post(
            reverse("catalog:dish-delete", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())
