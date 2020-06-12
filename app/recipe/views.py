from rest_framework.viewsets import ModelViewSet

from .models import Recipe

from .serializers import RecipeSerializer


class RecipeViewSet(ModelViewSet):
    """Recipe views"""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
