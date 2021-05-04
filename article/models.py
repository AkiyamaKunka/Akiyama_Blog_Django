from django.db import models

# Create your models here.
from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
# define the ORM relationship between Django and database

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # store at lease 100 characters
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # just like it says, added when it was created
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # the newer the higher
        ordering = ('-created',)
    def __str__(self):
        return self.title