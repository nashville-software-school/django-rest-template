from rest_framework import serializers
from models import Category

class CategorySerializer(serializers.Serializer):
    """This class will serialize data for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')