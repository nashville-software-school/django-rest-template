from django.db.models import Count
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from serializers import (PostSerializer, CreatePostSerializer, 
                        UpdatePostSerializer, CreateCommentSerializer, CommentSerializer)
from models import Post, Comment, Profile, Category
from datetime import datetime

class PostView(ViewSet):
    """This class will initialize methods of manipulating data"""
    def retrive(self, request, pk):
        """Get single post"""
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        "Get all posts"
        # later we will sort by comment count, data posted, recent activity, and title
        posts = Post.objects.all()
        serializer = PostSerializer(posts)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def categoryposts(self, request):
        """Get posts associated with category"""
        category = Category.objects.all()
        posts = Post.objects.all().filter(category=category)
        serializer = PostSerializer(posts)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create a post"""
        profile = Profile.objects.get(user=request.auth.user)
        created_on = datetime.now()
        serializer = CreatePostSerializer(data=request.data)
        serializer.save(profile=profile, created_on=created_on)
        
    def destroy(self, request, pk):
        """Delete a post"""
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        """Update a post"""
        post = Post.object.get(pk=pk)
        serializer = UpdatePostSerializer(data=request.data)
        serializer.save(post)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def comment(self, request):
        """Comment on a post"""
        pass
    
    @action(methods=['post', 'delete'], detail=True)
    def like(self, request, pk):
        """Like a post"""
        pass
