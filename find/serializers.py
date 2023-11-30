from rest_framework import serializers
from .models import FindPost, Comment, Reply


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('user_id', 'comment_id', 'content', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    replys = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('user_id', 'post_id', 'content', 'created_at', 'updated_at', 'replys')



class FindPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = FindPost
        fields = '__all__'
