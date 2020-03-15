from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='blog/posts/cover_images/')
    introduction = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


