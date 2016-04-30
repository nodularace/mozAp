# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160429_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polygonarea',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='polygonarea',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='date_updated',
        ),
    ]
