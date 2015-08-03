# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0024_ticker_server_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depth',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('asks', models.TextField()),
                ('bids', models.TextField()),
            ],
        ),
    ]
