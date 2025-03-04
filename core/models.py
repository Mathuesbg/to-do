from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    OPTIONS = [
        ('pending', "Pending"),
        ('completed', "Completed")
        ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=10, choices = OPTIONS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    
    def __str__(self):
        return self.title


