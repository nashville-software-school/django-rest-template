from rest_framework import serializers
from app_api.serializers import UserSerializer
from app_api.models import Post

class PostSerializer(serializers.Serializer):
    """This class will serialize data for get posts"""
    class Meta:
        model = Post
        fields = ('profile', 'text', 'category', 'created_on')
        depth = 1

class CreatePostSerializer(serializers.Serializer):
    """This class will serialize data for create posts"""
    class Meta:
        model = Post
        field = ['text', 'category']

class UpdatePostSerializer(serializers.Serializer):
    """This class will serialize data to update posts"""
    class Meta:
        model = Post
        field = ['text']       
