from django.urls import path
from .views import podcast_reviews, episode_reviews

urlpatterns = [
    path('podcast/<int:podcast_id>/', podcast_reviews, name='podcast_reviews'),
    path('episode/<int:episode_id>/', episode_reviews, name='episode_reviews'),
]