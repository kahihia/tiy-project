# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0020_remove_tradehistory_end_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradehistory',
            name='_From',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tradehistory',
            name='end_id',
            field=models.IntegerField(default=1000),
        ),
    ]
