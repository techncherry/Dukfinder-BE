from rest_framework import generics
from .models import NoticePost
from .serializers import NoticePostSerializer

class NoticePostListCreateView(generics.ListCreateAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

class NoticePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

