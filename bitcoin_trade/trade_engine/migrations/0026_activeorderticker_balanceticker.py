# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_engine', '0025_depth'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveOrderTicker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('json', jsonfield.fields.JSONField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='UserActiveOrders')),
            ],
        ),
        migrations.CreateModel(
            name='BalanceTicker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usd', models.DecimalField(max_digits=13, decimal_places=8)),
                ('btc', models.DecimalField(max_digits=10, decimal_places=8)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='UserBalance')),
            ],
        ),
    ]
