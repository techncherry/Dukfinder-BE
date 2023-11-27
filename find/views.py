from rest_framework import generics
from .models import Post, FindCategory
from .serializers import PostSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


class PostListByCategory(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Post.objects.filter(category__id=category_id)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

