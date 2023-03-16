from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    print(create_at)
    def __str__(self):
        return f'{self.create_at.month}/{self.create_at.day}에 생성된 {self.id}번글 - {self.title}: {self.content}'