# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trade_engine', '0003_auto_20150730_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='UserAccount'),
        ),
    ]
