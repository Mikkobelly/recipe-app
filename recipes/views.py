from django.shortcuts import render

# Create your views here.
def recipe_home(request):
    return render(request, 'recipes/recipe_home.html')