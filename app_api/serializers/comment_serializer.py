from rest_framework import serializers
from app_api.models import Comment

class CommentSerializer(serializers.Serializer):
    """This class will serialize data for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post__id', 'profile', 'created_on')
        depth = 1

class CreateCommentSerializer(serializers.Serializer):
    """This class will serialize data to create a comment"""
    class Meta:
        model = Comment
        fields = ['text']
