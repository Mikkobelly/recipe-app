from django.urls import path
from .views import recipe_home, RecipeListView, RecipeDetailView, records

app_name = 'recipes'

urlpatterns = [
    path('', recipe_home, name='home'),
    path('recipes/', RecipeListView.as_view(), name='list'),
    path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('records/', records, name='records')
]

