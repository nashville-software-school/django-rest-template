from rest_framework import serializers
from app_api.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """This class will serialize data for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')