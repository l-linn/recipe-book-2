from .models import Recipe


def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    # get_absolute_url() should take you to the detail page of book #1
    # and load the URL /books/list/1
    self.assertEqual(recipe.get_absolute_url(), "/recipes/list/1")
