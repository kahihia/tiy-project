# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_engine', '0011_remove_activeorder_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fromn', models.IntegerField(default=0)),
                ('count', models.IntegerField()),
                ('from_id', models.IntegerField(default=0)),
                ('end_id', models.IntegerField()),
                ('order', models.CharField(max_length=4, default='DESC')),
                ('since', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('pair', models.CharField(max_length=7, default='btc_usd')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
