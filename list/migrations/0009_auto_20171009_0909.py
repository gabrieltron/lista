# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-09 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0008_board_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='back',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='front',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='row',
            name='first_item',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='row',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
