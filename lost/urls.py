from django.urls import path, include
from .views import CategoryPostsView, LostPostListView, LostPostDetailView, ThisWeekPostsListView, ThisMonthPostsListView, LostPostSearchAPIView, LostPostCreateView, LostPostUpdateView



urlpatterns = [
    path('lost_posts/', LostPostListView.as_view(), name='post-list'),
    path('lost_posts/<int:pk>/', LostPostDetailView.as_view(), name='post-detail'),
    path('lost_posts/create', LostPostCreateView.as_view(), name='post-create'),
    path('lost_posts/<int:intLpk>/update/', LostPostUpdateView.as_view(), name='post-update'),
    path('lost_posts/this-week', ThisWeekPostsListView.as_view(), name='this-week-posts-list'),
    path('lost_posts/this-month', ThisMonthPostsListView.as_view(), name='this-month-posts-list'),
    path('lost_posts/category/<str:category>', CategoryPostsView.as_view(), name='category-posts'),
    path('lost_posts/search/', LostPostSearchAPIView.as_view(), name='post-search-api'),

]
