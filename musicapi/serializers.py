from rest_framework import serializers
from .models import Song,PodCast,AudioBook


class SongSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, required=True)
    # duration = serializers.IntegerField(default=0)

    class Meta:
        model = Song
        fields = "__all__"


class PodCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = PodCast
        fields = "__all__"


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioBook
        fields = "__all__"


class FileSerializer(serializers.Serializer):
    filetype = serializers.CharField(max_length=10)


class MusicSerializer(serializers.Serializer):
    podcast = PodCastSerializer(read_only=True, many=True)
    song = SongSerializer(read_only=True, many=True)
    audiobook = AudioBookSerializer(read_only=True, many=True)
