from django import forms
from .models import Podcast, Episode

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['title', 'description', 'category', 'language', 'image']

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['title', 'release_date', 'duration', 'show_notes']
