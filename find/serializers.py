from rest_framework import serializers
from .models import FindCategory, FindPost, FindComment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FindCategory
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = FindPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindComment
        fields = '__all__'