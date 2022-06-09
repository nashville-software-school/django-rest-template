from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Comment, Profile
from app_api.serializers import CommentSerializer, CreateCommentSerializer

class CommentView(ViewSet):
    """This class will handle methods of data for comments"""
    def list(self):
        """Get all comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Edit a post"""
        comment = Comment.objects.get(pk=pk)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.save(comment)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
