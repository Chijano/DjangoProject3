from django import forms
from .models import Review, EpisodeReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "text"]

class EpisodeReviewForm(forms.ModelForm):
    class Meta:
        model = EpisodeReview
        fields = ["rating", "text"]
