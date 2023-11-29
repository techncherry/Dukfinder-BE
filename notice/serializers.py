from rest_framework import serializers
from .models import NoticePost
from django.contrib.auth.models import User

class NoticePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticePost
        fields = ('id', 'title', 'content', 'notice_image', 'top_fixed', 'created_at', 'updated_at', 'view_count', 'author')

    def increase_views(self, instance):
        instance.view_count += 1
        instance.save()


class NoticePostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = '__all__'