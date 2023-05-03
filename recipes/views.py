from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_chart

# Create your views here.
def recipe_home(request):
    return render(request, 'recipes/recipe_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    chart = None

    if request.method == 'POST':
        difficulty = request.POST.get('difficulty')
        chart_type = request.POST.get('chart_type')

        all_records = Recipe.objects.all()
        id_searched = []
        for obj in all_records:
            if obj.calculate_difficulty().lower() == difficulty:
                id_searched.append(obj.id)
        qs = all_records.filter(id__in=id_searched)

        if qs:
            recipes_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['category'].values)
            recipes_df = recipes_df.to_html()
        elif difficulty == 'all':
            recipes_df = pd.DataFrame(all_records.values())
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['category'].values)
            recipes_df = recipes_df.to_html()

    context = {
        'form' : form,
        'recipes_df' : recipes_df,
        'chart' : chart
    }

    return render(request, 'recipes/records.html', context)
