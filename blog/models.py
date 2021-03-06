import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import *
from .fields import PhoneNumberField, ZipCodeField, PreZipCodeField


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목', validators=[MinLengthValidator(4)])
    content = models.TextField(help_text='Markdown문법을 써주세요.')
    lnglat = models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    text_field = models.IntegerField(default=10)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='blog_comment_set') # default = comment_set
    #Post객체명.blog_comment_set.all()
    author = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.message



class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Contact(models.Model):

    name = models.CharField(max_length=30)
    phone_number1 = PhoneNumberField()
    zip_code = ZipCodeField(blank=True)
    pre_zip_code = PreZipCodeField(blank=True)
    zip_test = models.CharField(max_length=20, validators=[ZipCodeValidator(True)])


# 우편번호는 바뀌지 않기 때문에 DB에 저장해놓고 db와 communication하는 것이 더 좋다.
class ZipCode(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    code = models.CharField(max_length=7)