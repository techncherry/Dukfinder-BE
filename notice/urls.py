from django.urls import path
from .views import NoticePostDetailView, NoticePostListCreateView

urlpatterns = [
    path('notice/', NoticePostListCreateView.as_view(), name='notice-list-create'),
    path('notice/<int:pk>/', NoticePostDetailView.as_view(), name='notice-detail'),
]