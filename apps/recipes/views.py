from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import RecipeSearchForm
from .utils import get_chart
from .models import Recipe
import pandas as pd


# Create your views here.
# The render function requires two arguments ( request and template) and returns an HttpResponse object with that rendered text.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")


def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)
    # df means DataFrame
    recipes_df = None
    chart = None

    # check if the button is clicked
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        chart_type = request.POST.get("chart_type")
        recipe_category = request.POST.get("recipe_category")
        cooking_time = request.POST.get("cooking_time")
        difficulty = request.POST.get("difficulty")

        cooking_time = 0 if not cooking_time else cooking_time
        recipe_category = "" if not recipe_category else recipe_category
        recipe_name = "" if not recipe_name else recipe_name
        difficulty = "" if not difficulty else difficulty

        # apply filter to extract data
        qs = Recipe.objects.filter(
            Q(name=recipe_name)
            | Q(category=recipe_category)
            | Q(cooking_time=cooking_time)
        )

        qs2 = [
            recipe
            for recipe in Recipe.objects.all()
            if recipe.difficulty() == difficulty
        ]  # qs2 is a list of recipes, need to change it back to query set

        # MyModel.objects.filter(id__in={instance.id for instance in instances})

        qs3 = Recipe.objects.filter(pk__in={recipe.pk for recipe in qs2})

        qs = (qs | qs3).distinct()

        if qs:
            recipes_df = pd.DataFrame(qs.values("name", "cooking_time", "category"))
            chart = get_chart(chart_type, recipes_df, labels=recipes_df["name"].values)
            print(recipes_df)

            # recipes_df.assign(Difficulty=[])
            recipes_df = recipes_df.to_html()

            for q in qs:
                item_id = q.id
                item_name = q.name  # get name of the recipe
                difficulty = q.difficulty()

                # breakpoint()

                recipes_df = recipes_df.replace(  # replace the table-name
                    f"<td>{item_name}</td>",
                    f"<td><a href ='/recipes/{item_id}' style='text-decoration: none'>{item_name}</td>",
                )

            print(recipes_df)

    # pack up data to be sent to template in the context dictionary
    context = {
        "form": form,
        "recipes_df": recipes_df,
        "chart": chart,
    }

    return render(request, "recipes/search_recipes.html", context)


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipes/all_recipes.html"  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_details.html"


# import pdb
# pdb.set_trace()
# qs = [q for q in qs if q.difficulty == recipe_difficulty]
