from django.urls import path
from .views import recipe_home
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', recipe_home),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/<pk>', RecipeDetailView.as_view(), name='detail')
]

