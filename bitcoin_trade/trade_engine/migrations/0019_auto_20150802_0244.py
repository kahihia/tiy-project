# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0018_auto_20150802_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradehistory',
            name='_From',
        ),
        migrations.RemoveField(
            model_name='tradehistory',
            name='end',
        ),
        migrations.RemoveField(
            model_name='tradehistory',
            name='since',
        ),
    ]
