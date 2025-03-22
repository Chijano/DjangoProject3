from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.podcast_list, name='podcast_list'),
    path('<int:podcast_id>/', views.podcast_detail, name='podcast_detail'),
    path('episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
