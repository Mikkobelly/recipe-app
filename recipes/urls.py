from django.urls import path
from .views import recipe_home

app_name = 'recipes'

urlpatterns = [
    path('', recipe_home)
]

