from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET'])
def check(request):
    return Response("OK")

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def create_post(request):
    title = request.data.get('title')
    content = request.data.get('content')

    if not title or not content:
        return Response({'error': 'Title and content are required'}, status=status.HTTP_400_BAD_REQUEST)

    post = Post(title=title, content=content, author=request.user)
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_list_post(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT',])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_update_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if post.author != request.user:
            return Response({'error': 'You are not authorized to update this post'}, status=status.HTTP_403_FORBIDDEN)
        
        title = request.data.get('title')
        content = request.data.get('content')

        if not title or not content:
            return Response({'error': 'Title and content are required'}, status=status.HTTP_400_BAD_REQUEST)

        post.title = title
        post.content = content
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list_create(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')

        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment(text=text, post=post, author=request.user)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.author != request.user:
        return Response({'error': 'You are not authorized to delete this post'}, status=status.HTTP_403_FORBIDDEN)
    post.delete()
    return Response("Post Deleted",status=status.HTTP_204_NO_CONTENT)

