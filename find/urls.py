# urls.py
from django.urls import path
from .views import PostListByCategory, PostListCreateView, PostDetailView

urlpatterns = [
    path('posts/<int:category_id>/', PostListByCategory.as_view(), name='post-list-by-category'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]
