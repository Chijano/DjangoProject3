from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, EpisodeReview
from podcasts.models import Podcast, Episode
from django.contrib.auth.decorators import login_required
from users.models import UserProfile  # Import UserProfile
from .forms import ReviewForm, EpisodeReviewForm  # You need to create these forms


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


@login_required
def podcast_reviews(request, podcast_id):
    """Display and add reviews for a specific podcast."""
    podcast = get_object_or_404(Podcast, id=podcast_id)
    reviews = Review.objects.filter(podcast=podcast)

    # Check if the logged-in user is a Listener
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.role.name != "Listener":
        return render(request, 'reviews/podcast_reviews.html', {
            'podcast': podcast, 'reviews': reviews, 'error': "Only Listeners can add reviews."
        })

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.podcast = podcast
            review.save()
            return redirect('podcast_reviews', podcast_id=podcast.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/podcast_reviews.html', {
        'podcast': podcast, 'reviews': reviews, 'form': form
    })


@login_required
def episode_reviews(request, episode_id):
    """Display and add reviews for a specific episode."""
    episode = get_object_or_404(Episode, id=episode_id)
    reviews = EpisodeReview.objects.filter(episode=episode)

    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.role.name != "Listener":
        return render(request, 'reviews/episode_reviews.html', {
            'episode': episode, 'reviews': reviews, 'error': "Only Listeners can add reviews."
        })

    if request.method == "POST":
        form = EpisodeReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.episode = episode
            review.save()
            return redirect('episode_reviews', episode_id=episode.id)
    else:
        form = EpisodeReviewForm()

    return render(request, 'reviews/episode_reviews.html', {
        'episode': episode, 'reviews': reviews, 'form': form
    })