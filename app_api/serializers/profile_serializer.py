from rest_framework import serializers
from app_api.models import Profile
from app_api.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    """This class will serialize data for get posts"""
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('id', 'profile_img', 'tags', 'bio', 'user', 'posts')
        depth = 1

class CreateProfileSerializer(serializers.ModelSerializer):
    """This class will serialize data for create posts"""
    class Meta:
        model = Profile
        fields = ['id', 'bio']
