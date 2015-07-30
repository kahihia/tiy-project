# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0002_auto_20150730_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='api_key',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='secret',
            field=models.CharField(max_length=100),
        ),
    ]
