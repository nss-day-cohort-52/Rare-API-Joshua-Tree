from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Post, RareUser

class CommentView(ViewSet):
    """Rare Comments view"""
    
    def list(self, request):
        """Handle GET requests to get all comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        """Handle GET requests to get a single comment by pk"""
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def create(self, request):
        """
        Handle POST requests to post a new comment
        -- Returns:
            Response -- JSON serialized game instance
        """
        author = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["post"])
        comment = Comment.objects.create(
            content=request.data["content"],
            author=author,
            post=post
        )
        serializer = CreateCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for Post Comments"""
    
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2
class CreateCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for posting new comment"""
    
    class Meta:
        model = Comment
        fields = ('content', 'author', 'post')