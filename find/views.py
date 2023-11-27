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

class ThisWeekPostsListView(generics.ListAPIView):
    serializer_class = FindPostSerializer

    def get_queryset(self):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = FindPost.objects.filter(created_at__range=[start_of_week, end_of_week])
        return queryset

class ThisMonthPostsListView(generics.ListAPIView):
    serializer_class = FindPostSerializer

    def get_queryset(self):
        today = timezone.now().date()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month + timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - timedelta(days=1)

        queryset = FindPost.objects.filter(created_at__range=[start_of_month, end_of_month])
        return queryset

class FindPostSearchAPIView(generics.ListAPIView):
    serializer_class = FindPostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return FindPost.objects.filter(Q(title__icontains=query))
