"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from rareapi.model.tags import Tags




class TagsView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        
        tag = Tags.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        tag = Tags.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        """Delete game"""
        tag = Tags.objects.get(pk=pk)
        tag.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tags
        fields = ('id','label')
        depth = 1