# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 23:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160504_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
