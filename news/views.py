from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, News, Video
from .serializers import CategorySerializer, NewsSerializer, VideoSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class NewsByCategoryView(APIView):
    def get(self, request, category_id):
        news = News.objects.filter(category_id=category_id)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class VideosByCategoryView(APIView):
    def get(self, request, category_id):
        videos = Video.objects.filter(category_id=category_id)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
