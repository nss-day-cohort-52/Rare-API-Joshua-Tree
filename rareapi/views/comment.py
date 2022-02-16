from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rareapi.model import Comment

class CommentView(ViewSet):
    """Rare Post Comments view"""
    
    def list(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def 
    
class CommentSerializer(ModelSerializer):
    """JSON serializer for Post Comments"""
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2
        