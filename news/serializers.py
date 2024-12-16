from rest_framework import serializers
from .models import Category, News, Video

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = News
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Video
        fields = '__all__'
