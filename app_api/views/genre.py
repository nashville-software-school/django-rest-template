from django.views import View
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Genre
from app_api.serializers import GenreSerializer

class GenreView(ViewSet):
    """This class will handle methods of data for genre"""
    def retrieve(self, pk):
        """Get a single genre"""
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Get all genres"""
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres)
        return Response(serializer.data)
