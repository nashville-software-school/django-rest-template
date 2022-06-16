from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from app_api.serializers import PostSerializer, CreatePostSerializer, UpdatePostSerializer, CreateCommentSerializer, CommentSerializer
from app_api.models import Post, Comment, Profile, Category
from datetime import datetime

class PostView(ViewSet):
    """This class will initialize methods of manipulating data"""
    def retrieve(self, request, pk):
        """Get single post"""
        try:
            post = Post.objects.get(pk=pk)
            post.is_my_post = request.auth.user == post.profile.user
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        "Get all posts"
        # later we will sort by comment count, data posted, recent activity, and title
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a post"""
        profile = Profile.objects.get(user=request.auth.user)
        created_on = datetime.now()
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=profile, created_on=created_on)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def destroy(self, request, pk):
        """Delete a post"""
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        """Update a post"""
        post = Post.objects.get(pk=pk)
        serializer = UpdatePostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def comment(self, request, pk):
        """Comment on a post"""
        profile = Profile.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=pk)
        created_on = datetime.now()
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_on=created_on, profile=profile, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post', 'delete'], detail=True)
    def like(self, request, pk):
        """Like a post"""
        pass
