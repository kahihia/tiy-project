# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0031_auto_20150811_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='type',
            field=models.CharField(max_length=4, choices=[('buy', 'buy'), ('sell', 'sell')]),
        ),
    ]
