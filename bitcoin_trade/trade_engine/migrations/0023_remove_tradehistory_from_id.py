# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0022_remove_tradehistory_end_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradehistory',
            name='from_id',
        ),
    ]
