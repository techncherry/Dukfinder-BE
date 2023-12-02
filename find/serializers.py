from rest_framework import serializers
from .models import FindPost, FindComment, FindReply


class FindReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = FindReply
        fields = ('user_id', 'comment_id', 'content', 'created_at', 'updated_at')


class FindCommentSerializer(serializers.ModelSerializer):
    replys = FindReplySerializer(many=True, read_only=True)

    class Meta:
        model = FindComment
        fields = ('user_id', 'post_id', 'content', 'created_at', 'updated_at', 'replys')



class FindPostSerializer(serializers.ModelSerializer):
    comments = FindCommentSerializer(many=True, read_only=True)
    class Meta:
        model = FindPost
        fields = '__all__'