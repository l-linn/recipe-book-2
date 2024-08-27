from django.urls import path
from .views import recipes_home, search_recipes, RecipeListView, RecipeDetailView

app_name = "recipes"

urlpatterns = [
    path("", recipes_home),
    path("search/", search_recipes),
    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
]
