from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Version 1.0 Required API endpoints

class CreateFile(APIView):
    # @staticmethod
    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            filetype = request.data.get("filetype")

            if filetype == "Song":
                serializer = SongSerializer(data=data)
                if serializer.is_valid():

                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif filetype == "AudioBook":
                serializer = AudioBookSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif filetype == "PodCast":
                serializer = PodCastSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "unrecognized file format"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_file(request, file, identifier):
    if file == "Song":
        try:
            song = Song.objects.get(pk=identifier)

        except Song.DoesNotExist:
            return Response({"message": "Audio does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif file == "AudioBook":

        try:
            audiobook = AudioBook.objects.get(pk=identifier)
        except AudioBook.DoesNotExist:
            return Response({"message": "Audio does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AudioBookSerializer(audiobook, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif file == "PodCast":
        try:
            podcast = PodCast.objects.get(pk=identifier)
        except PodCast.DoesNotExist:
            return Response({"message": "PodCast does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PodCastSerializer(instance=podcast, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            # return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Unrecognized file type {}".format(file)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_file(request, file, identifier):

    if file == "Song":
        try:
            song = Song.objects.get(pk=identifier)
        except Song.DoesNotExist:
           return Response({"message": "Song does not exist"}, status=status.HTTP_404_NOT_FOUND)

        song.delete()
        print("Song with id {} was deleted".format(identifier))
        return Response({"message": "song deleted"}, status=status.HTTP_200_OK)

    if file == "PodCast":
        try:
            podcast= PodCast.objects.get(pk=identifier)
        except PodCast.DoesNotExist:
            return Response({"message": "PodCast does not exist"}, status=status.HTTP_404_NOT_FOUND)

        podcast.delete()
        print("Podcast with id {} was deleted".format(identifier))
        return Response({"message": "PodCast deleted"}, status=status.HTTP_200_OK)

    if file == "AudioBook":
        try:
            audiobook= AudioBook.objects.get(pk=identifier)
        except AudioBook.DoesNotExist:
            return Response({"message": "AudioBook does not exist"}, status=status.HTTP_404_NOT_FOUND)

        audiobook.delete()
        print("AudioBook with id {} was deleted".format(identifier))
        return Response({"message": "AudioBook deleted"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def retrieve_file(request, file=None, identifier=None):
    if file == "Song":
        if not identifier:
            song = Song.objects.all()
            many = True

        else:
            try:
                song = Song.objects.get(pk=identifier)
                many = False
            except Song.DoesNotExist:
                return Response({"message": "Song does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SongSerializer(song, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if file == "PodCast":
        if not identifier:
            podcast = PodCast.objects.all()
            many = True

        else:
            try:
                podcast = PodCast.objects.get(pk=identifier)
                many = False
            except PodCast.DoesNotExist:
                return Response({"message": "Podcast does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PodCastSerializer(podcast, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if file == "AudioBook":

        if not identifier:
            audiobook = AudioBook.objects.all()
            many = True

        else:
            try:

                audiobook = AudioBook.objects.get(pk=identifier)
                many = False
            except AudioBook.DoesNotExist:

                return Response({"message": "Audiobook does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AudioBookSerializer(audiobook, many=many)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if not file:
        filters = {}
        filters['audiobook'] = AudioBook.objects.all()
        filters['podcast'] = PodCast.objects.all()
        filters['song'] = Song.objects.all()
        serializer = MusicSerializer(filters)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Version 2.0 Just had fun doing these

class SongListView(ListAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class SongRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()


class PodCastListView(ListAPIView):
    serializer_class = PodCastSerializer
    queryset = PodCast.objects.all()


class PodCastRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PodCastSerializer
    queryset = PodCast.objects.all()


class AudioBookListView(ListAPIView):
    serializer_class = AudioBookSerializer
    queryset = AudioBook.objects.all()


class AudioBookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AudioBookSerializer
    queryset = AudioBook.objects.all()


