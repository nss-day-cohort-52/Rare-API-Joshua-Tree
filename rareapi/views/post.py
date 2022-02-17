
from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rareapi.models import Post, RareUser, Tag, Category

class PostView(ViewSet):
    
    def create(self, request):
        user = RareUser.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category"])
        
        post = Post.objects.create(
            user = user,
            category = category,
            title = request.data['title'],
            publication_date = request.data['publication_date'],
            image_url = request.data['image_url'],
            content = request.data['content'],
            approved = request.data['approved']
        )
        
        try:
            post.tags.set(request.data['tags'])
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')
        depth = 2

