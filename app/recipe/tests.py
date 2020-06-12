from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Recipe, Ingredient

from .serializers import RecipeSerializer, IngredientSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    """Return the recipe detail URL"""
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_recipe(**params):
    """Creates a sample recipe"""
    defaults = {
        'name': 'Recipe name',
        'description': 'Recipe description'
    }
    defaults.update(params)

    return Recipe.objects.create(**defaults)


def sample_ingredient(**params):
    """Creates a sample ingredient"""
    defaults = {
        'name': 'Ingredient name'
    }
    defaults.update(params)

    return Ingredient.objects.create(**defaults)


class RecipeApiTests(TestCase):
    """Recipe API tests"""

    def setUp(self):
        self.client = APIClient()

    def test_get_recipe(self):
        """Test the retrieve endpoint"""
        recipe = sample_recipe()
        serialized_recipe = RecipeSerializer(recipe)

        url = detail_url(recipe.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized_recipe.data)

    def test_list_recipes(self):
        """Test the list endpoint"""
        sample_recipe(name='Recipe test 1', description='Recipe test 1 description')
        sample_recipe(name='Recipe test 2', description='Recipe test 2 description')

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all()
        serialized_recipes = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serialized_recipes.data)

    def test_create_recipe(self):
        """Test the create recipe endpoint"""
        payload = {
            'name': 'Recipe name',
            'description': 'Recipe description'
        }

        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_update_recipe(self):
        """Test the update recipe endpoint"""
        recipe = sample_recipe()
        payload = {
            'name': 'Updated recipe name',
            'description': 'Updated recipe description'
        }

        url = detail_url(recipe.id)
        self.client.put(url, payload)

        recipe.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_patch_recipe(self):
        """Test the patch recipe endpoint"""
        recipe = sample_recipe()
        payload = {
            'name': 'Updated recipe name',
            'description': 'Updated recipe description'
        }

        url = detail_url(recipe.id)
        self.client.patch(url, payload)

        recipe.refresh_from_db()
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_delete_recipe(self):
        """Test the delete recipe endpoint"""
        recipe = sample_recipe()

        url = detail_url(recipe.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Recipe.objects.count(), 0)
