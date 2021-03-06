# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-18 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_managers_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='managers',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='managers',
            name='email',
            field=models.EmailField(default='ac', max_length=255, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='managers',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='managers',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='managers',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
