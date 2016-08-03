# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 17:00
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160801_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='pre_zip_code',
            field=blog.fields.PreZipCodeField(default=1, max_length=7, validators=[blog.validators.pre_zipcode_validator]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number1',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]