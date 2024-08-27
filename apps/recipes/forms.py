from django import forms

CHART__CHOICES = (  # specify choices as a tuple
    ("#1", "Bar chart"),  # when user selects "Bar chart", it is stored as "#1"
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)
CAT_CHOICES = (
    ("", "select"),
    ("Versatile", "Versatile"),
    ("V", "V"),
    ("Ve", "Ve"),
    ("Fish", "Fish"),
    ("Contains Meat", "Contains Meat"),
)

DIF__CHOICES = (
    ("", "select"),
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Intermediate", "Intermediate"),
    ("Hard", "Hard"),
)


# define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
    )
    cooking_time = forms.IntegerField(required=False)
    recipe_category = forms.ChoiceField(choices=CAT_CHOICES, required=False)
    difficulty = forms.ChoiceField(choices=DIF__CHOICES, required=False)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES, required=False)
