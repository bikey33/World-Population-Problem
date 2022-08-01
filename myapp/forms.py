from django import forms
from .models import Country, Population
class PopulationForm(forms.ModelForm):
    class Meta:
        model = Population
        fields = ['city','man_population','woman_population','child_population']

