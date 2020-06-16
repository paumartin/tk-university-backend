from django.db import models


class Recipe(models.Model):
    """Recipe object"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Ingredient(models.Model):
    """Ingredient object"""
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    class Meta:
        unique_together = ('name', 'recipe')

    def __str__(self):
        return self.name
