# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0021_auto_20150802_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradehistory',
            name='end_id',
        ),
    ]
