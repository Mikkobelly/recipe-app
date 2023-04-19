from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Latte', cooking_time=3, ingredients='Grounded Coffee, Boiled Water, Warm Milk, Sugar', description='1. Make filtered coffee 2. Add warm milk 3. Add sugar')

    def test_recipe_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_cooking_time_help_text(self):
        recipe = Recipe.objects.get(id=1)
        help_text = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(help_text, 'In minutes')
    
    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 350)

    def test_calculte_difficulty(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Medium')

