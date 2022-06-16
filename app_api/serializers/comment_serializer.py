from rest_framework import serializers
from app_api.models import Comment
from app_api.serializers.profile_serializer import ProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    """This class will serialize data for comments"""
    profile = ProfileSerializer()
    is_my_comment = serializers.SerializerMethodField('get_author')
    def get_author(self, object):
        """custom method to get author of comment"""
        return object.profile.user == self.context['request'].auth.user
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'profile', 'created_on', 'is_my_comment')
        depth = 2

class CreateCommentSerializer(serializers.ModelSerializer):
    """This class will serialize data to create a comment"""
    class Meta:
        model = Comment
        fields = ['id', 'text']
