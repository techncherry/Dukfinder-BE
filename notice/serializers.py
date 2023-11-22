from rest_framework import serializers
from .models import NoticePost

class NoticePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoticePost
        fields = ('id', 'title', 'content', 'head_image', 'created_at', 'updated_at',  'author')