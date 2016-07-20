import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목') #한줄입력
    content = models.TextField(help_text='Markdown문법을 써주세요.') #여러줄 입력
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    text_field = models.IntegerField(default=10)
    tag = models.ManyToManyField('Tag', blank=True) #tag인스턴스명.post_set.all()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='blog_comment_set')
    #comment인스턴스명.post_set.all()
    #Post객체명.blog_comment_set.all()
    author = models.CharField(max_length=100)
    message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name