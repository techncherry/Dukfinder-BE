# urls.py
from django.urls import path
from .views import PostListByCategory, PostListCreateView, PostDetailView, CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/<int:category_id>/', PostListByCategory.as_view(), name='post-list-by-category'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
    # 다른 URL 패턴들을 추가할 수 있습니다.
]
