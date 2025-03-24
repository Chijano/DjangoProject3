from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=50)
    image = models.ImageField(upload_to='podcast_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=255)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name="episodes")
    release_date = models.DateField()
    duration = models.DurationField()
    show_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.podcast.title} - {self.title}"


class PodcastOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'podcast')  # Ensure one user owns a podcast

    def __str__(self):
        return f"{self.user.username} owns {self.podcast.title}"
