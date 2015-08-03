
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import jsonfield
import json
import http.client
import urllib.request, urllib.parse, urllib.error
import hashlib
import hmac
import time

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='UserAccount')
    api_key = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)


class Balance(models.Model):
    user = models.ForeignKey(User)


@receiver(post_save, sender=Balance)
def balance_handler(sender, instance, **kwargs):
    useraccount = instance.user.UserAccount
    api_key = useraccount.api_key
    secret = useraccount.secret.encode()
    user = instance.user
    nonce = str(((time.time() - 1398621111) * 10)).split('.')[0]
    parms = {"method": "getInfo",
             "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    parms = parms.encode()
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)
    response = conn.getresponse().read()
    response = response.decode('latin-1')
    response = json.loads(response)
    usd = response['return']['funds']['usd']
    btc = response['return']['funds']['btc']
    object = {'user': user, 'usd': usd, 'btc': btc}
    BalanceTicker.objects.create(**object)


class BalanceTicker(models.Model):
    user = models.ForeignKey(User, related_name='UserBalance')
    usd = models.DecimalField(max_digits=13, decimal_places=8)
    btc = models.DecimalField(max_digits=10, decimal_places=8)


class ActiveOrder(models.Model):
    user = models.ForeignKey(User)


@receiver(post_save, sender=ActiveOrder)
def active_order_handler(sender, instance, **kwargs):
    useraccount = instance.user.UserAccount
    api_key = useraccount.api_key
    secret = useraccount.secret.encode()
    user = instance.user
    nonce = str(((time.time() - 1398621111) * 10)).split('.')[0]
    parms = {"method": "ActiveOrders",
             "pair": "btc_usd",
             "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    parms = parms.encode()
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)
    response = conn.getresponse().read()
    response = response.decode('latin-1')
    response = json.loads(response)
    object = {'user': user, 'json': response}
    ActiveOrderTicker.objects.create(**object)


class ActiveOrderTicker(models.Model):
    user = models.ForeignKey(User, related_name='UserActiveOrders')
    json = jsonfield.JSONField()



class Trade(models.Model):
    user = models.ForeignKey(User)
    pair = models.CharField(max_length=8, default="btc_usd")
    type = models.CharField(max_length=4)
    rate = models.DecimalField(max_digits=13, decimal_places=8)
    amount = models.DecimalField(max_digits=10, decimal_places=8)


@receiver(post_save, sender=Trade)
def trade_handler(sender, instance, **kwargs):
    useraccount = instance.user.UserAccount
    api_key = useraccount.api_key
    secret = useraccount.secret.encode()
    user = instance.user
    nonce = str(((time.time() - 1398621111) * 10)).split('.')[0]
    parms = {"method": "Trade",
             "pair": instance.pair,
             "type": instance.type,
             "rate": instance.rate,
             "amount": instance.amount,
             "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    parms = parms.encode()
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)
    response = conn.getresponse().read()
    response = response.decode('latin-1')
    response = json.loads(response)
    object = {'user': user, 'json': response}
    TradeTicker.objects.create(**object)


class TradeTicker(models.Model):
    user = models.ForeignKey(User)
    json = jsonfield.JSONField()


class CancelOrder(models.Model):
    user = models.ForeignKey(User)
    order_id = models.IntegerField()


@receiver(post_save, sender=CancelOrder)
def cancel_order_handler(sender, instance, **kwargs):
    useraccount = instance.user.UserAccount
    api_key = useraccount.api_key
    secret = useraccount.secret.encode()
    user = instance.user
    nonce = str(((time.time() - 1398621111) * 10)).split('.')[0]
    parms = {"method": "CancelOrder",
             "order_id": instance.order_id,
             "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    parms = parms.encode()
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)
    response = conn.getresponse().read()
    response = response.decode('latin-1')
    response = json.loads(response)
    object = {'user': user, 'json': response}
    CancelOrderTicker.objects.create(**object)


class CancelOrderTicker(models.Model):
    user = models.ForeignKey(User)
    json = jsonfield.JSONField()


class TradeHistory(models.Model):
    user = models.ForeignKey(User)
    _From = models.IntegerField(default=0)
    count = models.IntegerField(default=1000)
    order = models.CharField(max_length=4, default="DESC")
    pair = models.CharField(max_length=7, default="btc_usd")


@receiver(post_save, sender=TradeHistory)
def trade_history_handler(sender, instance, **kwargs):
    useraccount = instance.user.UserAccount
    api_key = useraccount.api_key
    secret = useraccount.secret.encode()
    user = instance.user
    nonce = str(((time.time() - 1398621111) * 10)).split('.')[0]
    parms = {"method": "TradeHistory",
             "user": instance.user,
             "from": instance._From,
             "count": instance.count,
             "order": instance.order,
             "pair": instance.pair,
             "nonce": nonce}
    parms = urllib.parse.urlencode(parms)
    hashed = hmac.new(secret, digestmod=hashlib.sha512)
    parms = parms.encode()
    hashed.update(parms)
    signature = hashed.hexdigest()
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Key": api_key,
               "Sign": signature}
    conn = http.client.HTTPSConnection("btc-e.com")
    conn.request("POST", "/tapi", parms, headers)
    response = conn.getresponse().read()
    response = response.decode('latin-1')
    response = json.loads(response)
    object = {'user': user, 'json': response}
    TradeHistoryTicker.objects.create(**object)


class TradeHistoryTicker(models.Model):
    user = models.ForeignKey(User)
    json = jsonfield.JSONField()


class Ticker(models.Model):
    high = models.DecimalField(max_digits=6, decimal_places=2)
    low = models.DecimalField(max_digits=6, decimal_places=2)
    avg = models.DecimalField(max_digits=6, decimal_places=2)
    vol = models.DecimalField(max_digits=20, decimal_places=2)
    vol_cur = models.DecimalField(max_digits=9, decimal_places=2)
    server_time = models.IntegerField()
    last = models.DecimalField(max_digits=6, decimal_places=2)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    updated = models.IntegerField()


class Depth(models.Model):
    asks = models.TextField()
    bids = models.TextField()