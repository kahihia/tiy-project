# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0010_activeorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeorder',
            name='pair',
        ),
    ]
