from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = TaggableManager()

    def __str__(self):
        return self.title


