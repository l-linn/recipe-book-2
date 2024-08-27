from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    fav_recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes_fav")

    pic = models.ImageField(upload_to="recipes", default="no_picture.png")

    def __str__(self):
        return self.user.username
