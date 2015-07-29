# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('btc', models.DecimalField(decimal_places=8, max_digits=12)),
                ('usd', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CancelOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('high', models.DecimalField(decimal_places=2, max_digits=6)),
                ('low', models.DecimalField(decimal_places=2, max_digits=6)),
                ('avg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vol', models.DecimalField(decimal_places=2, max_digits=20)),
                ('vol_cur', models.DecimalField(decimal_places=2, max_digits=9)),
                ('last', models.DecimalField(decimal_places=2, max_digits=6)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6)),
                ('updated', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pair', models.CharField(default='btc_usd', max_length=8)),
                ('type', models.CharField(max_length=4)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=12)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('api_key', models.CharField(max_length=50)),
                ('secret', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
