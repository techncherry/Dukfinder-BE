from rest_framework import serializers
from .models import NoticePost

class NoticePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticePost
        fields = ('id', 'title', 'content', 'notice_image', 'top_fixed', 'created_at', 'updated_at', 'view_count', 'author')

    def increase_views(self, instance):
        instance.view_count += 1
        instance.save()


class NoticePostTitleDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = ('title', 'created_at', 'view_count')