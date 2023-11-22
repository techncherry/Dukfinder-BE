# views.py
from rest_framework import generics
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import NoticePost
from .serializers import NoticePostSerializer

class NoticePostListView(generics.ListAPIView):
    queryset = NoticePost.objects.order_by('-top_fixed', '-created_at')
    serializer_class = NoticePostSerializer

class NoticePostCreateView(generics.CreateAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('notice-list'))

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('notice-list'))


