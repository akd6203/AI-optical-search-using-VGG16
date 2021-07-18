from django import forms
from myapp.models import SearchResults

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchResults
        fields = ['title','image']