from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .models import LostPost
from django.utils import timezone
from datetime import timedelta
from .serializers import LostPostSerializer
from django.db.models import Q

class CategoryPostsView(generics.ListAPIView):
    serializer_class = LostPostSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return LostPost.objects.filter(category=category)


class LostPostListView(generics.ListAPIView): #lostpostlist
    queryset = LostPost.objects.all()
    serializer_class = LostPostSerializer


class LostPostDetailView(generics.RetrieveDestroyAPIView): #lostpostlistdetail, destory
    queryset = LostPost.objects.all()
    serializer_class = LostPostSerializer

class LostPostCreateView(CreateAPIView): #lostpostlistcreate
    queryset = LostPost.objects.all()
    serializer_class = LostPostSerializer

class LostPostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = LostPost.objects.all()
    serializer_class = LostPostSerializer
    lookup_url_kwarg = 'intLpk'  # Set the correct lookup field name


class ThisWeekPostsListView(generics.ListAPIView):
    serializer_class = LostPostSerializer

    def get_queryset(self):
        today = timezone.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        queryset = LostPost.objects.filter(created_at__range=[start_of_week, end_of_week])
        return queryset

class ThisMonthPostsListView(generics.ListAPIView):
    serializer_class = LostPostSerializer

    def get_queryset(self):
        today = timezone.now().date()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month + timedelta(days=32)
        end_of_month = end_of_month.replace(day=1) - timedelta(days=1)

        queryset = LostPost.objects.filter(created_at__range=[start_of_month, end_of_month])
        return queryset

class LostPostSearchAPIView(generics.ListAPIView):
    serializer_class = LostPostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return LostPost.objects.filter(Q(title__icontains=query))
