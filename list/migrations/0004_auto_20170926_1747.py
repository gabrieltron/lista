# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-26 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20170926_1723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List',
            new_name='UserList',
        ),
        migrations.RenameField(
            model_name='doing',
            old_name='list',
            new_name='user_list',
        ),
        migrations.RenameField(
            model_name='done',
            old_name='list',
            new_name='user_list',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='list',
            new_name='user_list',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='list',
            new_name='user_list',
        ),
    ]
