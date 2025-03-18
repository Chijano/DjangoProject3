from django.contrib.auth.models import User
from django.db import models
from podcasts.models import Podcast  # ✅ Import Podcast model

class Role(models.Model):
    ROLE_CHOICES = [
        ('Listener', 'Listener'),
        ('Podcaster', 'Podcaster'),
        ('Admin', 'Admin')
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    favorite_podcasts = models.ManyToManyField(Podcast, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username