from rest_framework import serializers
from app_api.models import Post
from app_api.serializers.comment_serializer import CommentSerializer
from app_api.serializers.profile_serializer import ProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    """This class will serialize data for get posts"""
    profile = ProfileSerializer()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'profile', 'title', 'text', 'category',
                  'created_on', 'comments', 'is_my_post')
        depth = 2

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
