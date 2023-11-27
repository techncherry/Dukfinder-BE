
from django.urls import path, include
from .views import CategoryPostsView, FindPostListView, FindPostDetailView, FindPostCreateView, FindPostUpdateView, \
    FindPostSearchAPIView

urlpatterns = [
    path('find_posts/', FindPostListView.as_view(), name='post-list'),
    path('find_posts/<int:pk>/', FindPostDetailView.as_view(), name='post-detail'),
    path('find_posts/create', FindPostCreateView.as_view(), name='post-create'),
    path('find_posts/<int:intLpk>/update/', FindPostUpdateView.as_view(), name='post-update'),
    path('find_posts/category/<str:category>', CategoryPostsView.as_view(), name='category-posts'),
    path('find_posts/search/', FindPostSearchAPIView.as_view(), name='post-search-api'),

]
