from django.db import models
# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PodCast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)
    narrator = models.CharField(max_length=100)

    def __str__(self):
        return self.title

