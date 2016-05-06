# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Dias',
            },
        ),
        migrations.AddField(
            model_name='pool',
            name='date_created',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='pool',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='tipo',
            field=models.CharField(choices=[(b'regular', b'Regular'), (b'irregular', b'Irregular')], max_length=10),
        ),
        migrations.AddField(
            model_name='pool',
            name='dias',
            field=models.ManyToManyField(blank=True, to='core.Dia'),
        ),
    ]