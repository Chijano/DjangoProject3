from django.urls import path
from django.conf import settings
from django.shortcuts import render
from django.conf.urls.static import static
from .views import podcast_list, podcast_detail, episode_detail, add_podcast, add_episode


def about(request):
    return render(request, 'about.html')


urlpatterns = [
    path('', podcast_list, name='podcast_list'),
    path('<int:podcast_id>/', podcast_detail, name='podcast_detail'),
    path('episode/<int:episode_id>/', episode_detail, name='episode_detail'),
    path('add/', add_podcast, name='add_podcast'),  # Add Podcast URL
    path('<int:podcast_id>/add_episode/', add_episode, name='add_episode'),  # Add Episode URL
    path('about/', about, name='about'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
