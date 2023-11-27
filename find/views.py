from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .models import FindPost
from django.utils import timezone
from datetime import timedelta
from .serializers import FindPostSerializer
from django.db.models import Q

class CategoryPostsView(generics.ListAPIView):
    serializer_class = FindPostSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return FindPost.objects.filter(category=category)


class FindPostListView(generics.ListAPIView): #Findpostlist
    queryset = FindPost.objects.all()
    serializer_class = FindPostSerializer


class FindPostDetailView(generics.RetrieveDestroyAPIView): #Findpostlistdetail, destory
    queryset = FindPost.objects.all()
    serializer_class = FindPostSerializer

class FindPostCreateView(CreateAPIView): #lostpostlistcreate
    queryset = FindPost.objects.all()
    serializer_class = FindPostSerializer

class FindPostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = FindPost.objects.all()
    serializer_class = FindPostSerializer
    lookup_url_kwarg = 'intLpk'


class FindPostSearchAPIView(generics.ListAPIView):
    serializer_class = FindPostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return FindPost.objects.filter(Q(title__icontains=query))
