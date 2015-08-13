# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0033_auto_20150812_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelorder',
            name='order_id',
            field=models.IntegerField(choices=[('776595153', '776595153')]),
        ),
        migrations.AlterField(
            model_name='cancelorder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
