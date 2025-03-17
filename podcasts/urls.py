from django.urls import path
from . import views

urlpatterns = [
    path('', views.podcast_list, name='podcast_list'),
    path('<int:podcast_id>/', views.podcast_detail, name='podcast_detail'),
    path('episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
]
