# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='test@gmail.com', max_length=100),
        ),
    ]
