from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='In minutes')
    ingredients = models.CharField(max_length=350, help_text='Ingredients must be separated by commas')
    description = models.TextField()

    def calculate_difficulty(self):
        ingredietns = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredietns) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredietns) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredietns) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredietns) >= 4:
            difficulty = 'Hard'
        return difficulty
    
    def __str__(self):
        return f"Recipe ID: {self.id}, Name: {self.name}"