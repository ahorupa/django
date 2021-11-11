from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.class Category (models.Model):


class category(models.Model):
    categorized = models.CharField(max_length=45)

    def __str__(self):
        return self.categorized


class Article (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    Description = models.TextField(max_length=5000)
    images = models.ImageField(blank=True, null=True, upload_to="media",)
    Editor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    Post_category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-posted_on']


class Reply(models.Model):
    idea = models.ForeignKey(
        Article, related_name="comments", on_delete=CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField(default="Your comments Please")
    igihe = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


# class Comment(models.Model):
#     post = models.ForeignKey(
#         Article, on_delete=models.CASCADE, related_name='comments')
#     commentor = models.CharField(max_length=200)
#     Email = models.EmailField()
#     commentbox = models.TextField()
#     time = models.DateTimeField(auto_now_add=True)

#     slug = models.SlugField(
#         verbose_name="Slug",
#         allow_unicode=True,
#         unique=True,
#         blank=True,
#         null=True)

#     class Meta:
#         ordering = ['time']

#     def __str__(self):
#         return self.idea
