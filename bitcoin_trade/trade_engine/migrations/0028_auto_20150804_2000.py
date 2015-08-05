# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trade_engine.custom_models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0027_cancelorderticker_tradehistoryticker_tradeticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depth',
            name='asks',
            field=trade_engine.custom_models.SeparatedValuesField(),
        ),
        migrations.AlterField(
            model_name='depth',
            name='bids',
            field=trade_engine.custom_models.SeparatedValuesField(),
        ),
    ]
