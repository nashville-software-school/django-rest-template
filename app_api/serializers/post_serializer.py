from rest_framework import serializers
from app_api.serializers.user_serializer import UserSerializer
from models import Post

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
        field = ['profile', 'text', 'category']