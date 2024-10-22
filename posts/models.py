from django.db import models


"""
Posts.objects.all() - все объекты из таблицы

Post.objects.filter(title="post") - все объекты по условию

Post.objects.get(id=1) - один объект по условию
"""

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=70)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return self.text











