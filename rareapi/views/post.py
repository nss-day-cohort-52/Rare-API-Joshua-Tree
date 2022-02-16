from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rareapi.model import Post, RareUser, Tag 

class PostView(ViewSet):
    
    def create(self, request):
        user = RareUser.objects.get(pk=request.auth.user_id)
        tags = []

        for tag_id in request.data['tags']:
            tag = Tag.objects.get(pk=tag_id)
            tags.append(tag)

        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid()
        post_obj = serializer.save(user=user)
        post_obj.tags.set(tags)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2

class CreatePostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'title', 'image_url', 'content', 'tags')