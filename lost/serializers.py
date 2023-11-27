from rest_framework import serializers
from .models import  LostPost
class LostPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = LostPost
        fields = '__all__'
