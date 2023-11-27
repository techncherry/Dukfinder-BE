from rest_framework import serializers
from .models import FindPost

class FindPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindPost
        fields = '__all__'
