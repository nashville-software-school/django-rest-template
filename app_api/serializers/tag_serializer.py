from rest_framework import serializers
from models import Tag

class TagSerializer(serializers.Serializer):
    """This class will serialize data for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'label')
