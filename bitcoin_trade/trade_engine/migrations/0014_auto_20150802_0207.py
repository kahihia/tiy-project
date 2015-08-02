# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0013_auto_20150802_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tradehistory',
            old_name='_from',
            new_name='_From',
        ),
    ]
