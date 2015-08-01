# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0005_auto_20150801_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='amount',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
    ]
