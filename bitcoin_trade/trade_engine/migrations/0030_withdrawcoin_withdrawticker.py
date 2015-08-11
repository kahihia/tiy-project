# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_engine', '0029_depositaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawCoin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('coin', models.CharField(default='BTC', max_length=3)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=8)),
                ('address', models.CharField(max_length=35)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawTicker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('amount', models.DecimalField(max_digits=10, decimal_places=8)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
