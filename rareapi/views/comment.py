from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment
from rareapi.models import Post

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
    
#    def create(self, request):
#        """
#        Handle POST requests to post a new comment
#        -- Returns:
#            Response -- JSON serialized game instance
#        """
#        serializer = CreateCommentSerializer(data=request.data)
#        import pdb; pdb.set_trace()
#        serializer.is_valid(raise_exception=True)
#        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def create(self, request):
        
        # retrieve author and post objects from the dbase to make sure they really exist; data retrieved is held in request.data dictionary.
        author = 
        post = Post.objects.get(pk=request.data["post"])
        

        # call "create" ORM (Object Relational Mapping) as pass fields as parameters to the function
        comment = Comment.objects.create(
            content=request.data["content"],
            author=request.data["author"],
            post=request.data["post"],
        )

        # created object is now serialized into dictionary version for json and returned to client
        serializer = CreateCommentSerializer(comment)
        return Response(serializer.data)

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