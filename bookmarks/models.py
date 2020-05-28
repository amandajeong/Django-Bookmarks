from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url


class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    link_id = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)

    def __str__(self):
        return self.name
