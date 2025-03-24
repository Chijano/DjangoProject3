from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from podcasts.models import Podcast, Episode, PodcastOwner, Category
from users.models import UserProfile
from .forms import PodcastForm, EpisodeForm
from podcasts.models import PodcastOwner


# Podcast Listing
def podcast_list(request):
    category_id = request.GET.get('category')
    language = request.GET.get('language')

    podcasts = Podcast.objects.all().order_by('title')

    if category_id:
        podcasts = podcasts.filter(category_id=category_id)

    if language:
        podcasts = podcasts.filter(language=language)

    podcast_owners = {po.podcast.id: po.user.username for po in PodcastOwner.objects.select_related('user', 'podcast')}

    for podcast in podcasts:
        podcast.owner_name = podcast_owners.get(podcast.id, "Unknown")

    categories = Category.objects.all()
    languages = Podcast.objects.values_list('language', flat=True).distinct()  # Get unique languages

    return render(request, 'podcast_templates/podcast_list.html', {
        'podcasts': podcasts,
        'categories': categories,
        'languages': languages,
        'selected_category': int(category_id) if category_id else None,
        'selected_language': language
    })


# Podcast Details
def podcast_detail(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    episodes = podcast.episodes.all().order_by('-release_date')

    # Fetch the actual owner of the podcast
    owner = PodcastOwner.objects.filter(podcast=podcast).first()
    owner_name = owner.user.username if owner else "Unknown"

    # Check if the logged-in user owns the podcast
    is_owner = request.user.is_authenticated and owner and owner.user == request.user

    return render(request, 'podcast_templates/podcast_detail.html', {
        'podcast': podcast,
        'episodes': episodes,
        'is_owner': is_owner,
        'owner_name': owner_name  # Pass owner name to template
    })




# Episode Details
def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    return render(request, 'podcast_templates/episode_detail.html', {
        'episode': episode
    })


# Add Podcast (Only Podcasters)
@login_required
def add_podcast(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.role.name != "Podcaster":
        return redirect('podcast_list')

    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save()
            PodcastOwner.objects.create(user=request.user, podcast=podcast)
            return redirect('podcast_list')
    else:
        form = PodcastForm()

    return render(request, 'podcast_templates/add_podcast.html', {'form': form})


# Add Episode (Only Owner of the Podcast)
@login_required
def add_episode(request, podcast_id):
    podcast = get_object_or_404(Podcast, id=podcast_id)
    if not PodcastOwner.objects.filter(user=request.user, podcast=podcast).exists():
        return redirect('podcast_detail', podcast_id=podcast.id)

    if request.method == 'POST':
        form = EpisodeForm(request.POST)
        if form.is_valid():
            episode = form.save(commit=False)
            episode.podcast = podcast
            episode.save()
            return redirect('podcast_detail', podcast_id=podcast.id)
    else:
        form = EpisodeForm()

    return render(request, 'podcast_templates/add_episode.html', {
        'form': form, 'podcast': podcast
    })


# Homepage with Top Podcasts and Episodes
def homepage(request):
    top_podcasts = Podcast.objects.annotate(avg_rating=Avg('reviews__rating')) \
                       .order_by('-avg_rating')[:3]
    top_episodes = Episode.objects.annotate(avg_rating=Avg('episode_reviews__rating')) \
                       .order_by('-avg_rating')[:3]

    # Fetch owners for top podcasts
    podcast_owners = {po.podcast.id: po.user.username for po in PodcastOwner.objects.select_related('user', 'podcast')}

    # Attach owner name to each top podcast object
    for podcast in top_podcasts:
        podcast.owner_name = podcast_owners.get(podcast.id, "Unknown")

    return render(request, 'homepage.html', {
        'top_podcasts': top_podcasts,
        'top_episodes': top_episodes
    })