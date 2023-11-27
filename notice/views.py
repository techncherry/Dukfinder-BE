from rest_framework import generics, mixins
from rest_framework.response import Response
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import NoticePost
from .serializers import NoticePostSerializer, NoticePostListSerializer

class NoticePostListView(generics.ListAPIView):
    queryset = NoticePost.objects.order_by('-top_fixed', '-created_at')
    serializer_class = NoticePostListSerializer

class NoticePostCreateView(generics.CreateAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_create(self, serializer):
        serializer.save()
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_destroy(self, instance):
        instance.delete()
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_update(self, serializer):
        serializer.save()
        return HttpResponseRedirect(reverse('notice-list'))


