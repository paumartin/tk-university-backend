from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Recipe

from .serializers import RecipeSerializer, IngredientSerializer


class RecipeViewSet(ModelViewSet):
    """Recipe views"""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(methods=['POST'], detail=True, url_path='ingredients')
    def add_ingredient(self, request, pk=None):
        """Adds an ingredient to a recipe"""
        ingredient_serializer = IngredientSerializer(data=request.data)
        recipe = self.get_object()

        if not ingredient_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ingredient_serializer.save(recipe=recipe)
        return Response(ingredient_serializer.data, status=status.HTTP_200_OK)
