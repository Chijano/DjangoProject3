from django.db import models
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.query} ({self.timestamp})"
