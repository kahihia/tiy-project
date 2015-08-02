# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0014_auto_20150802_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradehistory',
            name='count',
            field=models.IntegerField(default=1000),
        ),
    ]
