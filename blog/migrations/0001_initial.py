# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 04:45
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(help_text='Markdown문법을 써주세요.')),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('lnglat', models.CharField(help_text='경도, 위도 포맷으로 입력', max_length=50, validators=[blog.models.lnglat_validator])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=10)),
            ],
        ),
    ]
