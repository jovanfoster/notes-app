from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    pass


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    author = models.ForeignKey(CustomUser, related_name='notes', on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
