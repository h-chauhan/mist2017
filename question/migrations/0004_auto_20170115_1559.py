# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20161224_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='script',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
