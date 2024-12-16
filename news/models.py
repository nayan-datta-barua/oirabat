from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news")
    facebook_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Assuming you have a frontend route for each news article
        base_url = "https://yourdomain.com/news/"  # Replace with your actual domain
        news_url = f"{base_url}{self.id}/"  # Construct the news-specific URL
        self.facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={news_url}"
        super().save(*args, **kwargs)



class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="videos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # Assuming you have a frontend route for each news article
        base_url = "https://yourdomain.com/news/"  # Replace with your actual domain
        news_url = f"{base_url}{self.id}/"  # Construct the news-specific URL
        self.youtube_url = f"https://www.youtube.com/sharer/sharer.php?u={news_url}"
        super().save(*args, **kwargs)


