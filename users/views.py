from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .models import Role, UserProfile

def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users_templates/profile.html', {'user': user})

def user_list_view(request):
    users = User.objects.all()
    return render(request, "users_templates/users_list.html", {"users": users})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role_id = request.POST.get("role")  # Get role ID

        print(f"🛑 DEBUG: Selected Role ID from Form: {role_id}")  # Debugging step 1

        if not username or not password or not role_id:
            messages.error(request, "All fields are required.")
            return redirect("register")

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        # Create the user
        user = User.objects.create_user(username=username, password=password)

        # Fetch the correct role
        role = Role.objects.filter(id=role_id).exclude(name="Admin").first()
        print(f"🛑 DEBUG: Assigned Role from DB: {role.name if role else 'None'}")  # Debugging step 2

        if not role:
            messages.error(request, "Invalid role selection.")
            return redirect("register")

        # Ensure a profile doesn't already exist, then assign the role
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.role = role  # Explicitly assign the selected role
        profile.save()
        print(f"✅ DEBUG: Role Successfully Saved in DB: {profile.role.name}")  # Debugging step 3

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")

    # Fetch roles excluding Admin
    roles = Role.objects.exclude(name="Admin")
    return render(request, "users_templates/register.html", {"roles": roles})
