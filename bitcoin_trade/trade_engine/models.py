from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    api_key = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)


class Balance(models.Model):
    user = models.ForeignKey(User)
    btc = models.DecimalField(max_digits=12, decimal_places=8)
    usd = models.DecimalField(max_digits=5, decimal_places=2)


class Trade(models.Model):
    user = models.ForeignKey(User)
    pair = models.CharField(max_length=8, default="btc_usd")
    type = models.CharField(max_length=4)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=8)


class CancelOrder(models.Model):
    user = models.ForeignKey(User)
    order_id = models.IntegerField()


class Ticker(models.Model):
    high = models.DecimalField(max_digits=6, decimal_places=2)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    avg = models.DecimalField(max_digits=6, decimal_places=2)
    vol = models.DecimalField(max_digits=20, decimal_places=2)
    vol_cur = models.DecimalField(max_digits=9, decimal_places=2)
    last = models.DecimalField(max_digits=6, decimal_places=2)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    updated = models.IntegerField()
