from rest_framework import serializers
from app_api.models import Profile, Post
from app_api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    """This class will serialize data for get posts"""
    class Meta:
        model = Post
        fields = ('id', 'profile', 'title', 'text', 'category',
                  'created_on', 'comments', 'is_my_post', 'comment_count')
        depth = 2

class ProfileSerializer(serializers.ModelSerializer):
    """This class will serialize data for get posts"""
    user = UserSerializer()
    posts = PostSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('id', 'profile_img', 'tags', 'bio', 'user', 'posts', 'is_my_profile', 'songs')
        depth = 1

class CreateProfileSerializer(serializers.ModelSerializer):
    """This class will serialize data for create posts"""
    class Meta:
        model = Profile
        fields = ['id', 'bio']
