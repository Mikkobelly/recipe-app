from django import forms

DIFFICULTY_CHOICES = (
    ('all', 'All'),
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

class RecipeSearchForm(forms.Form):
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)