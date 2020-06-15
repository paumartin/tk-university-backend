from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Recipe, Ingredient


class IngredientSerializer(ModelSerializer):
    """Serializer for the ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class RecipeSerializer(ModelSerializer):
    """Serializer for the recipe object"""

    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'ingredients',)
        read_only_fields = ('id', 'ingredients',)
