"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.model import RareUser



class RareUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        
        rare_user = RareUser.objects.get(pk=pk)
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        rare_user = RareUser.objects.all()
        serializer = RareUserSerializer(rare_user, many=True)
        return Response(serializer.data)
    
    
    
class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = RareUser
        fields = ('id','created_on', 'bio', 'active', 'user')
        depth = 2