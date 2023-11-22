from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('find_posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('find_posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('find_comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('find_comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]