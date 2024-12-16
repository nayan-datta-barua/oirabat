from django.contrib import admin
from .models import Category, News ,Video

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'facebook_url', 'created_at')

@admin.register(Video)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'youtube_url', 'created_at')
