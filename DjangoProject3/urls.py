from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from podcasts.views import homepage
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('podcasts/', include('podcasts.urls')),
    path('users/', include('users.urls')),
    path('reviews/', include('reviews.urls')),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='users_templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users_templates/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

