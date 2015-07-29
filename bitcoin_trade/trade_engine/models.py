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