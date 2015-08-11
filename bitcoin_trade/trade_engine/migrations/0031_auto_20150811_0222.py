# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_engine', '0030_withdrawcoin_withdrawticker'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransHistory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_From', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=1000)),
                ('order', models.CharField(max_length=4, default='DESC')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransHistoryTicker',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('json', jsonfield.fields.JSONField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='depositaddress',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='UserAddress'),
        ),
    ]
