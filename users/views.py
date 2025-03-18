from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users_templates/profile.html', {'user': user})

def user_list_view(request):
    users = User.objects.all()
    return render(request, "users_templates/users_list.html", {"users": users})