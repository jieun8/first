# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pockemon', '0003_auto_20160718_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pockemon',
            name='catched_when',
            field=models.DateTimeField(null=True),
        ),
    ]