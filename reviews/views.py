from django.shortcuts import render, get_object_or_404
from .models import Review, EpisodeReview
from podcasts.models import Podcast, Episode

def podcast_reviews(request, podcast_id):
    """Display and add reviews for a specific podcast."""
    podcast = get_object_or_404(Podcast, id=podcast_id)
    reviews = Review.objects.filter(podcast=podcast)
    return render(request, 'reviews/podcast_reviews.html', {'podcast': podcast, 'reviews': reviews})

def episode_reviews(request, episode_id):
    """Display and add reviews for a specific episode."""
    episode = get_object_or_404(Episode, id=episode_id)
    reviews = EpisodeReview.objects.filter(episode=episode)
    return render(request, 'reviews/episode_reviews.html', {'episode': episode, 'reviews': reviews})
