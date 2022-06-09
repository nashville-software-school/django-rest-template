from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Tag
from app_api.serializers import TagSerializer

class TagView(ViewSet):
    """This class will handle methods of data for tags"""
    def retrieve(self, pk):
        """Get a single tag"""
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Get all tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags)
        return Response(serializer.data)
