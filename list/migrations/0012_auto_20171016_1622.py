# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-16 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_auto_20171016_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='first_element',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='back',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='front',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='row',
            name='back',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='row',
            name='first_element',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='row',
            name='front',
            field=models.IntegerField(default=None),
        ),
    ]
