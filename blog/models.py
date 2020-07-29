from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    replies = models.ManyToOneRel
    class Meta:
        ordering = ['date']

    def __str__(self):
        return '{} by {} id:{}'.format(self.title, self.author, self.id)


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='mainPost')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replyAuthor')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return '{}: {}'.format(self.author, self.message)


