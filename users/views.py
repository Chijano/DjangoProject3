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
        form = UserCreationForm(request.POST)
        role_id = request.POST.get("role")  # Get role ID from form

        if form.is_valid():
            user = form.save()

            print("Selected Role ID:", role_id)  # ✅ Debugging

            # Get the role instance
            role = Role.objects.filter(id=role_id).first()

            if role:
                print("Assigned Role:", role.name)  # ✅ Debugging

                # ✅ Explicitly set and save the role
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                user_profile.role = role  # Assign role
                user_profile.save(force_update=True)  # Force saving

                # 🔴 New Debugging Print - Check if role is actually saved
                saved_role = UserProfile.objects.get(user=user).role
                print("🛑 DEBUG: Role saved in DB:", saved_role)

                messages.success(request, "Registration successful! You are now logged in.")
            else:
                messages.warning(request, "Invalid role selected. Please update your profile.")

            login(request, user)  # Log in the user
            return redirect("homepage")  # Redirect to homepage

    else:
        form = UserCreationForm()

    roles = Role.objects.exclude(name="Admin")  # Exclude Admin role
    return render(request, "users_templates/register.html", {"form": form, "roles": roles})