from rest_framework import serializers
from app_api.models import Comment
from app_api.serializers.profile_serializer import ProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    """This class will serialize data for comments"""
    profile = ProfileSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'profile', 'created_on', 'is_my_comment')
        depth = 2

class CreateCommentSerializer(serializers.ModelSerializer):
    """This class will serialize data to create a comment"""
    class Meta:
        model = Comment
        fields = ['text']
