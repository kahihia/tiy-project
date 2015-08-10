from urllib.request import urlopen
import json
from matplotlib import pylab
from pylab import *
import numpy as np
import pandas as pd
from django_pandas.io import read_frame
from django.db.models import Avg
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from trade_engine.mixins import AddActiveOrderFormMixin
from trade_engine.models import UserAccount, ActiveOrder, ActiveOrderTicker, Balance, BalanceTicker, Trade, TradeTicker, CancelOrder, CancelOrderTicker, TradeHistory, TradeHistoryTicker, Ticker, Depth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from trade_engine.forms import BalanceForm, ActiveOrderForm, TradeForm, CancelOrderForm, TradeHistoryForm
from trade_engine.converter import *


def base(request):
    context = {"balance_ticker": BalanceTicker.objects.all()[BalanceTicker.objects.count()-1],
               "active_order_ticker": ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1],
               "ticker": Ticker.objects.all()[Ticker.objects.count()-1],
               "depth": Depth.objects.all()[Depth.objects.count()-1]}
    return render_to_response("base.html", context, context_instance=RequestContext(request))


def indicators(request):
    bull = False
    null = False
    bear = False
    lastprice = Ticker.objects.all()[Ticker.objects.count()-1]
    twoprice = Ticker.objects.all()[Ticker.objects.count()-2]
    threeprice = Ticker.objects.all()[Ticker.objects.count()-3]
    fourprice = Ticker.objects.all()[Ticker.objects.count()-4]
    one = lastprice.last
    two = twoprice.last
    three = threeprice.last
    four = fourprice.last
    if one > two and one > three and one > four:
        bull = True
        null = False
        bear = False
    elif one < two and one < three and one < four:
        bull = False
        null = False
        bear = True
    else:
        bull = False
        null = True
        bear = False
    bull_long = False
    null_long = False
    bear_long = False
    allpricemean = Ticker.objects.all().aggregate(Avg('last')).pop('last__avg', 0)
    print(allpricemean)
    if one > (allpricemean-(0.05*allpricemean)):
        bull_long = True
        null_long = False
        bear_long = False
    elif one < (allpricemean+(0.05*allpricemean)):
        bull_long = False
        null_long = False
        bear_long = True
    else:
        bull_long = False
        null_long = True
        bear_long = False
    context = {"bull": bull,
               "null": null,
               "bear": bear,
               "bull_long": bull_long,
               "null_long": null_long,
               "bear_long": bear_long}
    qs = Ticker.objects.all()
    df = read_frame(qs, coerce_float=True).convert_objects(convert_numeric=True, convert_dates=True)
    x = Depth.objects.all()[Depth.objects.count()-1].split_bids
    list1_bids = []
    list2_bids = []
    for item in x:
        itemlist = item.split(',')
        list1_bids.append(float(itemlist[0]))
        list2_bids.append(float(itemlist[1]))
    y = Depth.objects.all()[Depth.objects.count()-1].split_asks
    list1_asks = []
    list2_asks = []
    for item in y:
        itemlist = item.split(',')
        list1_asks.append(float(itemlist[0]))
        list2_asks.append(float(itemlist[1]))
    df1 = {'x': list1_bids,
           'y': list2_bids}
    df2 = {'x': list1_asks,
           'y': list2_asks}
    bids_frame = pd.DataFrame(df1)
    asks_frame = pd.DataFrame(df2)
    graph_one = scatter_to_base64(df, "plot_current_price")
    graph_two = scatter_to_base64(df, "plot_high")
    graph_low = scatter_to_base64(df, "plot_low")
    graph_avg = scatter_to_base64(df, "plot_avg")
    graph_vol = scatter_to_base64(df, "plot_vol")
    graph_three = scatter_to_base64(bids_frame, "plot_bids")
    graph_four = scatter_to_base64(asks_frame, "plot_asks")
    context["graph_one"] = graph_one
    context["graph_two"] = graph_two
    context["graph_low"] = graph_low
    context["graph_avg"] = graph_avg
    context["graph_vol"] = graph_vol
    context["graph_three"] = graph_three
    context["graph_four"] = graph_four
    return render_to_response("indicators.html", context, context_instance=RequestContext(request))


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2,
        })
        try:
            form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                                      {'form': form},
                                      context_instance=RequestContext(request)
                                      )
    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request)
                              )


def account_settings(request):
    context = {"balance_ticker": BalanceTicker.objects.all()[BalanceTicker.objects.count()-1],
               "active_order_ticker": ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1],
               "ticker": Ticker.objects.all()[Ticker.objects.count()-1],
               "depth": Depth.objects.all()[Depth.objects.count()-1]}
    return render_to_response('account_settings.html', context, context_instance=RequestContext(request))


def ticker_view(request):
    btce_prices = urlopen('https://btc-e.com/api/2/btc_usd/ticker')
    str_response = btce_prices.readall().decode('utf-8')
    btcejson = json.loads(str_response)
    ticker_obj = btcejson['ticker']
    Ticker.objects.create(**ticker_obj)
    context = {"balance_ticker": BalanceTicker.objects.all()[BalanceTicker.objects.count()-1],
               "active_order_ticker": ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1],
               "ticker": Ticker.objects.all()[Ticker.objects.count()-1],
               "depth": Depth.objects.all()[Depth.objects.count()-1]}
    return render_to_response('base.html', context, context_instance=RequestContext(request))


def depth_view(request):
    btce_depth = urlopen('https://btc-e.com/api/3/depth/btc_usd')
    str_response = btce_depth.readall().decode('utf-8')
    btcejson = json.loads(str_response)
    depth_obj = btcejson['btc_usd']
    print(depth_obj)
    Depth.objects.create(**depth_obj)
    context = {"balance_ticker": BalanceTicker.objects.all()[BalanceTicker.objects.count()-1],
               "active_order_ticker": ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1],
               "ticker": Ticker.objects.all()[Ticker.objects.count()-1],
               "depth": Depth.objects.all()[Depth.objects.count()-1]}
    return render_to_response('base.html', context, context_instance=RequestContext(request))


class CreateBalanceFormView(CreateView):

    model = Balance
    template_name = 'base.html'
    success_url = reverse_lazy('base')
    form_class = BalanceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateActiveOrderFormView(CreateView):

    model = ActiveOrder
    template_name = 'base.html'
    success_url = reverse_lazy('base')
    form_class = ActiveOrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateTradeFormView(CreateView):

    model = Trade
    template_name = 'trade.html'
    success_url = reverse_lazy('create_trade_form')
    form_class = TradeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateTradeFormView, self).get_context_data(**kwargs)
        ctx['balance_ticker'] = BalanceTicker.objects.all()[BalanceTicker.objects.count()-1]
        ctx['active_order_ticker'] = ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1]
        ctx['ticker'] = Ticker.objects.all()[Ticker.objects.count()-1]
        ctx['depth'] = Depth.objects.all()[Depth.objects.count()-1]
        return ctx

class CreateCancelOrderView(CreateView):

    model = CancelOrder
    template_name = 'cancel_trade.html'
    success_url = reverse_lazy('create_cancel_order_view')
    form_class = CancelOrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateCancelOrderView, self).get_context_data(**kwargs)
        ctx['balance_ticker'] = BalanceTicker.objects.all()[BalanceTicker.objects.count()-1]
        ctx['active_order_ticker'] = ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1]
        ctx['ticker'] = Ticker.objects.all()[Ticker.objects.count()-1]
        ctx['depth'] = Depth.objects.all()[Depth.objects.count()-1]
        return ctx


class CreateTradeHistoryView(CreateView):

    model = TradeHistory
    template_name = 'trade_history.html'
    success_url = reverse_lazy('trade_history_view')
    form_class = TradeHistoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateTradeHistoryView, self).get_context_data(**kwargs)
        ctx['balance_ticker'] = BalanceTicker.objects.all()[BalanceTicker.objects.count()-1]
        ctx['active_order_ticker'] = ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1]
        ctx['ticker'] = Ticker.objects.all()[Ticker.objects.count()-1]
        ctx['depth'] = Depth.objects.all()[Depth.objects.count()-1]
        return ctx


class CreateUserAccountView(CreateView):
    model = UserAccount
    template_name = "create_user_account.html"
    success_url = reverse_lazy('account_settings')
    fields = ["api_key", "secret"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(CreateUserAccountView, self).get_context_data(**kwargs)
        ctx['balance_ticker'] = BalanceTicker.objects.all()[BalanceTicker.objects.count()-1]
        ctx['active_order_ticker'] = ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1]
        ctx['ticker'] = Ticker.objects.all()[Ticker.objects.count()-1]
        ctx['depth'] = Depth.objects.all()[Depth.objects.count()-1]
        return ctx


class DeleteUserAccountView(DeleteView):
    model = UserAccount
    success_url = reverse_lazy('account_settings')


class UpdateUserAccountView(UpdateView):
    model = UserAccount
    template_name = "update_user_account.html"
    fields = ["api_key", "secret"]
    success_url = reverse_lazy('account_settings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return render(self.request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(UpdateUserAccountView, self).get_context_data(**kwargs)
        ctx['balance_ticker'] = BalanceTicker.objects.all()[BalanceTicker.objects.count()-1]
        ctx['active_order_ticker'] = ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1]
        ctx['ticker'] = Ticker.objects.all()[Ticker.objects.count()-1]
        ctx['depth'] = Depth.objects.all()[Depth.objects.count()-1]
        return ctx