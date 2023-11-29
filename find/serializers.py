from rest_framework import serializers
from .models import FindCategory, Post,  FindLocation

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FindCategory
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindLocation
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'location', 'date_select', 'content', 'head_image', 'created_at', 'updated_at',  'author')
