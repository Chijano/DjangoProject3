from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('podcasts/', include('podcasts.urls')),  # Podcasts app URLs
    path('users/', include('users.urls')),  # Users app URLs
    path('reviews/', include('reviews.urls')),  # Reviews app URLs
    path("search/", include("search.urls")),
]