from django.test import TestCase
from .models import Cook
from apps.recipes.models import Recipe
from django.contrib.auth.models import User


# Create your tests here.
class CookTestCase(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username="Craig", password="12345")

        fav_recipes = Recipe(name="Tacos", cooking_time=5, serves=2)
        fav_recipes.save()

        cook = Cook.objects.create(user=user)
        cook.fav_recipes.add(fav_recipes)

    def test_user(self):
        # Get a cook object to test
        cook = Cook.objects.get(id=1)
        # Get the metadata for the 'user' field and use it to query its data
        field_label = cook._meta.get_field("user").verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, "user")

    def test_user_username(self):
        cook = Cook.objects.get(id=1)
        self.assertEqual(cook.user.username, "Craig")

    def test_has_fav_recipes(self):
        cook = Cook.objects.get(id=1)
        fav_recipes_count = cook.fav_recipes.count()
        self.assertTrue(fav_recipes_count > 0)
