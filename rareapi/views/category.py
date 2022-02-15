"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.model import Category


class CategoryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        category = Category.objects.get(pk=pk) 
        # needs to be serialized because it is coming back as a python object and needs to be json
        serializer = CategoryTypeSerializer(category)
        #changed to json
        return Response(serializer.data)
    

    def list(self, request):
        category = Category.objects.all()
        serializer = CategoryTypeSerializer(category, many=True)
        return Response(serializer.data)
    
    
      
    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CategoryTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Category
        fields = ('id', 'label')
        
