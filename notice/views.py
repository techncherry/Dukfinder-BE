from rest_framework import generics, mixins
from rest_framework.response import Response
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import NoticePost
from .serializers import NoticePostSerializer, NoticePostListSerializer

class NoticePostListView(generics.ListAPIView): #공지사항 리스트
    queryset = NoticePost.objects.order_by('-top_fixed', '-created_at')
    serializer_class = NoticePostListSerializer

class NoticePostCreateView(generics.CreateAPIView): #공지사항 작성
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def perform_create(self, serializer):
        serializer.save()
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostDetailView(generics.RetrieveDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Call the increase_views method to increment the view count
        serializer.increase_views(instance)

        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()
        return HttpResponseRedirect(reverse('notice-list'))
