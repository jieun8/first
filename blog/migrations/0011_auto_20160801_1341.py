# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 04:41
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160801_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number1',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip_test',
            field=models.CharField(max_length=20, validators=[blog.validators.ZipCodeValidator(True)]),
        ),
    ]
