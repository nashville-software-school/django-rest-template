from rest_framework import serializers
from app_api.models import Category
from app_api.serializers.post_serializer import PostSerializer

class CategorySerializer(serializers.ModelSerializer):
    """This class will serialize data for categories"""
    posts = PostSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'label', 'posts')
        depth = 1