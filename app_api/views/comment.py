from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Comment, Profile
from app_api.serializers import CommentSerializer, CreateCommentSerializer

class CommentView(ViewSet):
    """This class will handle methods of data for comments"""
    def retrieve(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.is_my_post = request.auth.user == comment.profile.user
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Get all comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Edit a comment"""
        comment = Comment.objects.get(pk=pk)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.save(comment)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
