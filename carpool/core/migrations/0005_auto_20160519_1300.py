# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160506_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='contacto_email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pool',
            name='contacto_telefono',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pool',
            name='hora',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]