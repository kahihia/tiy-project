# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0034_auto_20150812_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelorder',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
