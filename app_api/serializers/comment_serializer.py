from rest_framework import serializers
from app_api.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """This class will serialize data for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post__id', 'profile', 'created_on')
        depth = 1

class CreateCommentSerializer(serializers.ModelSerializer):
    """This class will serialize data to create a comment"""
    class Meta:
        model = Comment
        fields = ['text']
