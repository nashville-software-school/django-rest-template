from rest_framework import serializers
from app_api.models import Post

class PostSerializer(serializers.ModelSerializer):
    """This class will serialize data for get posts"""
    class Meta:
        model = Post
        fields = ('id', 'profile', 'title', 'text', 'category', 'created_on', 'comments')
        depth = 1

class CreatePostSerializer(serializers.ModelSerializer):
    """This class will serialize data for create posts"""
    class Meta:
        model = Post
        fields = ['id', 'text', 'title','category']

class UpdatePostSerializer(serializers.ModelSerializer):
    """This class will serialize data to update posts"""
    class Meta:
        model = Post
        fields = ['id', 'text']       
