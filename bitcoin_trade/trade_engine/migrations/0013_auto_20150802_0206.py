# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0012_tradehistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tradehistory',
            old_name='fromn',
            new_name='_from',
        ),
    ]
