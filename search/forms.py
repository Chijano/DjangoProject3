from django import forms
from podcasts.models import Category  # Import Category model for filtering

class SearchForm(forms.Form):
    query = forms.CharField(label="Search", required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="All Categories")
    language = forms.CharField(label="Language", required=False)
    release_date = forms.DateField(label="Episode Release Date", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
