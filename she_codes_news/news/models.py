from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateField()
    url = models.URLField(max_length=200, default="")
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    category = models.ForeignKey('news.Category', related_name='stories', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Comment(models.Model):
    story = models.ForeignKey(
        NewsStory,
        related_name="comments",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
