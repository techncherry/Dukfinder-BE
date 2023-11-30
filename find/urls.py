from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryPostsView, FindPostListView, FindPostDetailView, ThisWeekPostsListView, \
    ThisMonthPostsListView, FindPostSearchAPIView, FindPostCreateView, FindPostUpdateView, \
    CommentViewSet, ReplyViewSet

urlpatterns = [
    path('find_posts/', FindPostListView.as_view(), name='post-list'),
    path('find_posts/<int:pk>/', FindPostDetailView.as_view(), name='post-detail'),
    path('find_posts/create/', FindPostCreateView.as_view(), name='post-create'),
    path('find_posts/<int:intLpk>/update/', FindPostUpdateView.as_view(), name='post-update'),
    path('find_posts/this-week/', ThisWeekPostsListView.as_view(), name='this-week-posts-list'),
    path('find_posts/this-month/', ThisMonthPostsListView.as_view(), name='this-month-posts-list'),
    path('find_posts/category/<str:category>', CategoryPostsView.as_view(), name='category-posts'),
    path('find_posts/search/', FindPostSearchAPIView.as_view(), name='post-search-api'),
    path('find_posts/<int:pk>/comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('find_posts/<int:post_pk>/comment/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment-detail'),
    path('find_posts/<int:pk>/reply/', ReplyViewSet.as_view({'get': 'list', 'post': 'create'}), name='reply-list'),
    path('find_posts/<int:post_pk>/reply/<int:pk>/', ReplyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reply-detail'),
]
