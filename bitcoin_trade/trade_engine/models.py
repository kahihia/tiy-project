from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import http.client
import urllib.request, urllib.parse, urllib.error
import json
import hashlib
import hmac
import time

class UserAccount(models.Model):
    user = models.ForeignKey(User)
    api_key = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)


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


@receiver(post_save, sender=Trade)
def my_handler(sender, instance, **kwargs):
    useraccount = UserAccount.objects.get(user=instance.user)
    api_key = useraccount.api_key
    secret = useraccount.secret
    nonce = int(((time.time() - 1398621111) * 10).split('.')[0])
    parms = {"method": "Trade",
              "pair": instance.pair,
              "type": instance.type,
              "rate": instance.rate,
              "amount": instance.amount,
              "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)

    response = conn.getresponse()
    print(response.status, response.reason)


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
