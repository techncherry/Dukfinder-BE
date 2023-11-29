from rest_framework import serializers
from .models import LostPost, Comment



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("pk", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class LostPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = LostPost
        fields = '__all__'



