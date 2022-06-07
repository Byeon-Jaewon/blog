from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4

from blog.storages import S3ImageStorage


def date_upload_to(instance, filename):
  # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
  # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
  # 결합 후 return
    return '/'.join([
        uuid_name + extension,
    ])


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="제목")
    content = models.CharField(max_length=1024, verbose_name="내용")
    image = models.ImageField(upload_to=date_upload_to,
                              storage=S3ImageStorage,
                              null=True, blank=True, verbose_name="이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성")
