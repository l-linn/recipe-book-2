from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    cook = models.ForeignKey(
        "cooks.Cook",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    cooking_time = models.IntegerField(
        help_text="Please input how long it takes in minutes"
    )

    category_choices = (
        ("V", "V"),
        ("Ve", "VE"),
        ("Fish", "Fish"),
        ("Contains Meat", "Contains Meat"),
        ("Versatile", "Versatile"),
    )
    category = models.CharField(
        max_length=50, choices=category_choices, default="versatile"
    )

    serves = models.PositiveIntegerField()
    ingredient = models.ManyToManyField("recipes.Ingredient")
    methods = models.TextField()
    pic = models.ImageField(upload_to="recipes", default="no_picture.png")

    def difficulty(self):
        num_ingredients = self.ingredient.count()

        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        else:
            return "Hard"

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    def display_ingredients(self):
        return ", ".join(ingredient.name for ingredient in self.ingredient.all())

    def __str__(self):
        return f"{self.name} - {self.cook} - {self.cooking_time} - {self.difficulty()}"
