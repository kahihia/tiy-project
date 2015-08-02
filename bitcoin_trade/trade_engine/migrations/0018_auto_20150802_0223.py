# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0017_auto_20150802_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradehistory',
            name='end_id',
            field=models.IntegerField(),
        ),
    ]
