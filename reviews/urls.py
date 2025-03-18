from django.urls import path
from .views import podcast_reviews, episode_reviews

urlpatterns = [
    # Reviews for a specific podcast
    path('podcast/<int:podcast_id>/', podcast_reviews, name='podcast-reviews'),

    # Reviews for a specific episode
    path('episode/<int:episode_id>/', episode_reviews, name='episode-reviews'),
]