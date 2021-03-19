from rest_framework.test import APIRequestFactory, APIClient, APITestCase
# from django.urls import resolve, reverse
from rest_framework import status
# from .models import PodCast, Song, AudioBook
# from .serializers import AudioBookSerializer, PodCastSerializer, MusicSerializer, SongSerializer, FileSerializer
# Create your tests here.

factory = APIRequestFactory()
client = APIClient()


class CreateFileTest(APITestCase):
    def test_song_creation(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "Song"}
        response = self.client.post("/api/v1/create/", data)
        # print(response)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_audio_book_creation(self):
        data = {"title": "Wild Child", "author": "Enya", "duration": 3600, "filetype": "AudioBook", "narrator": "The Just"}
        response = self.client.post("/api/v1/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pod_cast_creation(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "PodCast",
                "host": "Enya", "participants": "James, John"}
        response = self.client.post("/api/v1/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateTest(APITestCase):
    def test_song_update(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "Song"}
        response = self.client.post("/api/v1/create/", data)
        update_data = {"name": "Flora's Secret", "duration": 1000, "filetype": "Song"}
        update_response = self.client.put("/api/v1/update/Song/{}".format(response.data["id"]), update_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(update_response.data['name'], update_data["name"])
        self.assertEqual(update_response.data['duration'], update_data['duration'])
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

    def test_audio_book_update(self):
        data = {"title": "Wild Child", "author": "Enya", "duration": 3600, "filetype": "AudioBook", "narrator": "The Just"}
        response = self.client.post("/api/v1/create/", data)
        update_data = {"title": "Wild Child", "author": "Enya", "duration": 1000, "filetype": "AudioBook", "narrator": "James the Just"}
        update_response = self.client.put("/api/v1/update/AudioBook/{}".format(response.data["id"]), update_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(update_response.data['title'], update_data["title"])
        self.assertEqual(update_response.data['duration'], update_data['duration'])
        self.assertEqual(update_response.data['author'], update_data['author'])
        self.assertEqual(update_response.data['narrator'], update_data['narrator'])
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

    def test_pod_cast_update(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "PodCast",
                "host": "Enya", "participants": "James, John"}
        response = self.client.post("/api/v1/create/", data)

        update_data = {"name": "On my way home", "duration": 1000, "filetype": "PodCast",
                "host": "Enya Band", "participants": "Jude, James, Just"}
        update_response = self.client.put("/api/v1/update/PodCast/{}".format(response.data["id"]), update_data)
        # print(update_response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(update_response.data['name'], update_data["name"])
        self.assertEqual(update_response.data['duration'], update_data['duration'])
        self.assertEqual(update_response.data['host'], update_data['host'])
        self.assertEqual(update_response.data['participants'], update_data['participants'])
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)


class DeleteAudio(APITestCase):
    def test_song_delete(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "Song"}
        response = self.client.post("/api/v1/create/", data)
        update_data = {"name": "Flora's Secret", "duration": 1000, "filetype": "Song"}
        delete_response = self.client.delete("/api/v1/delete/Song/{}".format(response.data["id"]), update_data)
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)

    def test_audio_book_delete(self):
        data = {"title": "Wild Child", "author": "Enya", "duration": 3600, "filetype": "AudioBook", "narrator": "The Just"}
        response = self.client.post("/api/v1/create/", data)
        delete_response = self.client.delete("/api/v1/delete/AudioBook/{}".format(response.data["id"]))
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)

    def test_pod_cast_delete(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "PodCast",
                "host": "Enya", "participants": "James, John"}
        response = self.client.post("/api/v1/create/", data)

        update_data = {"name": "On my way home", "duration": 1000, "filetype": "PodCast",
                "host": "Enya Band", "participants": "Jude, James, Just"}
        delete_response = self.client.delete("/api/v1/delete/PodCast/{}".format(response.data["id"]), update_data)
        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)


class RetrieveAudio(APITestCase):
    def test_song_retrieve(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "Song"}
        response = self.client.post("/api/v1/create/", data)
        retrieve_response = self.client.get("/api/v1/retrieve/Song/{}".format(response.data['id']))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)

    def test_audio_book_retrieve(self):
        data = {"title": "Wild Child", "author": "Enya", "duration": 3600, "filetype": "AudioBook", "narrator": "The Just"}
        response = self.client.post("/api/v1/create/", data)
        retrieve_response = self.client.get("/api/v1/retrieve/AudioBook/{}".format(response.data['id']))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)

    def test_pod_cast_retrieve(self):
        data = {"name": "Wild Child", "duration": 3600, "filetype": "PodCast",
                "host": "Enya", "participants": "James, John"}
        response = self.client.post("/api/v1/create/", data)
        retrieve_response = self.client.get("/api/v1/retrieve/PodCast/{}".format(response.data['id']))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)


