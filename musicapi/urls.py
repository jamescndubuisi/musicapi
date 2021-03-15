from .views import (retrieve_file, SongListView,
                    SongRetrieveUpdateDestroy, AudioBookListView,
                    AudioBookRetrieveUpdateDestroy, PodCastListView,
                    PodCastRetrieveUpdateDestroy, CreateFile,
                    update_file, delete_file)
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()


# Could be separated into individual routes

urlpatterns = [
    # version 1.0
    path('v1/retrieve/<str:file>/', retrieve_file),
    path('v1/retrieve/', retrieve_file),
    path('v1/retrieve/<str:file>/<str:identifier>', retrieve_file),
    path('v1/create/', CreateFile.as_view()),
    path('v1/delete/<str:file>/<str:identifier>', delete_file),
    path('v1/update/<str:file>/<str:identifier>', update_file),

    # version 2.0 the fun part
    path('v2/song/', SongListView.as_view()),
    path('v2/song/<int:pk>', SongRetrieveUpdateDestroy.as_view()),
    path('v2/audiobook/', AudioBookListView.as_view()),
    path('v2/audiobook/<int:pk>', AudioBookRetrieveUpdateDestroy.as_view()),
    path('v2/podcast/', PodCastListView.as_view()),
    path('v2/podcast/<int:pk>', PodCastRetrieveUpdateDestroy.as_view()),
]
