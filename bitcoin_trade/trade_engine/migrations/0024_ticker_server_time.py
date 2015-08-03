# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0023_remove_tradehistory_from_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='server_time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
