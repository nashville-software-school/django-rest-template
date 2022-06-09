from os import stat
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Profile
from app_api.serializers import ProfileSerializer, CreateProfileSerializer

# we need to retrieve, list, create, and delete profiles
# we also might need a custom method to add music to a profile
class ProfileView(ViewSet):
    """This view will handle methods for data in profile"""
    def retrieve(self, pk):
        """Get a single profile"""
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Get all profiles"""
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a profile"""
        pass
    
    def update(self, request, pk):
        """Update a profile"""
        pass
    
    def destroy(self, request, pk):
        """Delete a profile"""
        profile = Profile.objects.get(pk=pk)
        profile.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
