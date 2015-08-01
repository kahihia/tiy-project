# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0004_auto_20150801_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='amount',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]
