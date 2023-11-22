# views.py
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import NoticePost
from .serializers import NoticePostSerializer, NoticePostTitleDateSerializer

class NoticePostListView(generics.ListAPIView):
    queryset = NoticePost.objects.order_by('-top_fixed', '-created_at')
    serializer_class = NoticePostTitleDateSerializer

class NoticePostCreateView(generics.CreateAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('notice-list'))

class NoticePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Increase views using the serializer method
        serializer.increase_views(instance)

        return Response(serializer.data)

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



