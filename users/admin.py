from django.contrib import admin
from .models import Role, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")  # Ensure role is displayed
    search_fields = ("user__username", "role__name")

admin.site.register(UserProfile, UserProfileAdmin)