from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.models import Tag
from django.contrib.auth.models import User

class UserView(ViewSet):
    """This class will handle methods of data for users"""
    def destroy(self, request, pk):
        """Delete a user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
