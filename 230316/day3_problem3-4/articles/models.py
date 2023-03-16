# 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

# 작성해야 하는 명령어
# python manage.py makemigrations
# python manage.py migrate