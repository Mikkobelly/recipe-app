from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    category_choices = [
        ('main', 'Main'),
        ('side', 'Side'),
        ('dessert', 'Dessert')
    ]

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=12, choices=category_choices, default='main')
    cooking_time = models.FloatField(help_text='In minutes')
    serving = models.PositiveIntegerField(default=1)
    ingredients = models.CharField(max_length=350, help_text='Ingredients must be separated by commas')
    directions = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no-image.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty
    
    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Recipe ID: {self.id}, Name: {self.name}"