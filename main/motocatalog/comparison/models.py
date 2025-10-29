from django.db import models

from django.contrib.auth.models import User

class ComparisonSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ComparisonItem(models.Model):
    session = models.ForeignKey(ComparisonSession, on_delete=models.CASCADE)
    motorcycle = models.ForeignKey('motorcycles.Motorcycle', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
