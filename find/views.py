from rest_framework import generics
from .models import Post, FindComment, FindCategory
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
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

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return FindComment.objects.filter(parent=None)

    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent')
        if parent_id:
            parent_comment = get_object_or_404(FindComment, pk=parent_id)
            serializer.save(user=self.request.user, parent=parent_comment)
        else:
            serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FindComment.objects.all()
    serializer_class = CommentSerializer
