from rest_framework import serializers
from app_api.models import Profile
from app_api.serializers import UserSerializer

class ProfileSerializer(serializers.Serializer):
    """This class will serialize data for get posts"""
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('id', 'profile_img', 'tags', 'bio', 'user')
        depth = 1

class CreateProfileSerializer(serializers.Serializer):
    """This class will serialize data for create posts"""
    class Meta:
        model = Profile
        field = ['tags', 'bio']
