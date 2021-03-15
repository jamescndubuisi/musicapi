from django.contrib import admin
from .models import AudioBook, PodCast, Song

# Register your models here.
admin.site.register(AudioBook)
admin.site.register(PodCast)
admin.site.register(Song)