# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0008_auto_20150801_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='btc',
        ),
        migrations.RemoveField(
            model_name='balance',
            name='usd',
        ),
    ]
