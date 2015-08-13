# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0032_auto_20150812_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelorder',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, choices=[('776595153', '776595153')]),
        ),
    ]
