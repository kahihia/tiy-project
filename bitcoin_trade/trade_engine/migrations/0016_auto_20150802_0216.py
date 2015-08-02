# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0015_auto_20150802_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradehistory',
            name='end_id',
            field=models.IntegerField(default=float("inf")),
        ),
    ]
