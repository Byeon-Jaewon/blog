from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="제목")
    content = models.CharField(max_length=1024, verbose_name="내용")
    image = models.ImageField(upload_to = "images/", null=True, blank=True, verbose_name="이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성")