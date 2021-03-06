# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolygonArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=8)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Provider')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
