from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from podcasts.models import Podcast, Episode
from django.db.models import Avg


def podcast_list(request):
    podcasts = Podcast.objects.all().order_by('title')
    return render(request, 'podcast_templates/podcast_list.html', {'podcasts': podcasts})

def podcast_detail(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    episodes = podcast.episodes.all().order_by('-release_date')
    return render(request, 'podcast_templates/podcast_detail.html', {'podcast': podcast, 'episodes': episodes})

def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    return render(request, 'podcast_templates/episode_detail.html', {'episode': episode})

def user_list_view(request):
    users = User.objects.all()
    return render(request, "users_templates/users_list.html", {"users": users})


def homepage(request):
    # Get top 3 rated podcasts
    top_podcasts = Podcast.objects.annotate(avg_rating=Avg('reviews__rating')) \
                       .order_by('-avg_rating')[:3]

    # Get top 3 rated episodes
    top_episodes = Episode.objects.annotate(avg_rating=Avg('episode_reviews__rating')) \
                       .order_by('-avg_rating')[:3]

    context = {
        'top_podcasts': top_podcasts,
        'top_episodes': top_episodes,
    }
    return render(request, 'homepage.html', context)

