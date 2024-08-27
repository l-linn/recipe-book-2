from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm


# Create your tests here.
class RecipeTestCase(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,
            serves=1,
            methods="boil the water, put the tea in",
        )

    def testRecipeName(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class SearchRecipeTestCase(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Tea",
            cooking_time=5,  # this is set as a choice
            serves=1,
            category="V",
            methods="boil the water, put the tea in",
        )

    def test_recipe_form_field_labels(self):
        form = RecipeSearchForm()
        self.assertTrue(
            form.fields["chart_type"].label is None
            or form.fields["chart_type"].label == "Chart type"
        )

    def test_chart_generation(self):
        form_data = {
            "recipe_name": "",
            "cooking_time": 10,
            "chart_type": "#1",
            "recipe_category": "V",
        }
        response = self.client.get("/search/", form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("chart" in response.context)
