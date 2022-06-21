from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Music, Profile
from app_api.serializers import MusicSerializer, CreateMusicSerializer
from django.core.files.base import ContentFile
import base64
import uuid

class MusicView(ViewSet):
    def retrieve(self, request, pk):
        """Get a single song"""
        try:
            music = Music.objects.get(pk=pk)
            serializer = MusicSerializer(music)
            return Response(serializer.data)
        except Music.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """List all songs"""
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Upload a song"""
        profile = Profile.objects.get(user=request.auth.user)
        format, imgstr = request.data["song"].split(';base64,')
        ext = format.split('/')[-1]
        request.data['song'] = ContentFile(base64.b64decode(imgstr), name=f'{request.auth.user.id}-{uuid.uuid4()}.{ext}')
        genres = request.data['genres']
        serializer = CreateMusicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=profile)
        return Response(None, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        """Delete a song"""
        music = Music.objects.get(pk=pk)
        music.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
