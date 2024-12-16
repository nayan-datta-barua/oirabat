

from django.urls import path
from .views import CategoryListView, NewsByCategoryView, VideosByCategoryView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/news/', NewsByCategoryView.as_view(), name='news-by-category'),
    path('categories/<int:category_id>/videos/', VideosByCategoryView.as_view(), name='videos-by-category'),
]
