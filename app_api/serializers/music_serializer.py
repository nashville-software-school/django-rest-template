from rest_framework import serializers
from models import Music

class MusicSerializer(serializers.Serializer):
    """This class will serialize data for music"""
    class Meta:
        model = Music
        fields = ('id', 'song', 'genres')

class CreateMusicSerializer(serializers.Serializer):
    """This class will serialize data for music"""
    class Meta:
        model = Music
        fields = ['song', 'genres']
