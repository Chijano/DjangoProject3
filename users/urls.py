from django.urls import path
from .views import user_profile_view, user_list_view

urlpatterns = [
    path('profile/<str:username>/', user_profile_view, name='user-profile'),
    path('all/', user_list_view, name='user-list'),
]
