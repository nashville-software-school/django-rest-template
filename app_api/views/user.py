from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Tag
from django.contrib.auth.models import User
from app_api.serializers import UserSerializer, UpdateUserSerializer

class UserView(ViewSet):
    """This class will handle methods of data for users"""
    def retrieve(self, request, pk):
        """Get a single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """Update a user"""
        user = User.objects.get(pk=pk)
        serializer = UpdateUserSerializer(user, data=request.data)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete a user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
