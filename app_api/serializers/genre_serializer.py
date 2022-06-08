from rest_framework import serializers
from models import Genre

class GenreSerializer(serializers.Serializer):
    """This class will serialize data for genres"""
    class Meta:
        model = Genre
        fields = ('id', 'label')
