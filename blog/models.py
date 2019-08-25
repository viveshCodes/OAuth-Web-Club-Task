from django.db import models


# Create your models here.
class Look(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pic = models.ImageField(default='default.jpg',blank=True)
    date = models.DateTimeField(auto_now_add=True)