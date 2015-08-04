from urllib.request import urlopen
import json
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from trade_engine.mixins import AddActiveOrderFormMixin
from trade_engine.models import UserAccount, ActiveOrder, ActiveOrderTicker, Balance, BalanceTicker, Trade, TradeTicker, CancelOrder, CancelOrderTicker, TradeHistory, TradeHistoryTicker, Ticker, Depth
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from trade_engine.forms import BalanceForm, ActiveOrderForm, TradeForm, CancelOrderForm, TradeHistoryForm


def base(request):
    context = {"balance_ticker": BalanceTicker.objects.all()[BalanceTicker.objects.count()-1],
               "active_order_ticker": ActiveOrderTicker.objects.latest(field_name="json"),
               "ticker": Ticker.objects.latest(field_name="last"),
               "depth": Depth.objects.all()[Depth.objects.count()-1]}
    return render_to_response("base.html", context, context_instance=RequestContext(request))


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
               "active_order_ticker": ActiveOrderTicker.objects.latest(field_name="json"),
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
               "active_order_ticker": ActiveOrderTicker.objects.latest(field_name="json"),
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
               "active_order_ticker": ActiveOrderTicker.objects.latest(field_name="json"),
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
        return super().form_valid(form)


class CreateCancelOrderView(CreateView):

    model = CancelOrder
    template_name = 'cancel_trade.html'
    success_url = reverse_lazy('create_cancel_order_view')
    form_class = CancelOrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateTradeHistoryView(CreateView):

    model = TradeHistory
    template_name = 'trade_history.html'
    success_url = reverse_lazy('trade_history_view')
    form_class = TradeHistoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CreateUserAccountView(CreateView):
    model = UserAccount
    template_name = "create_user_account.html"
    success_url = reverse_lazy('account_settings')
    fields = ["api_key", "secret"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
        return super().form_valid(form)