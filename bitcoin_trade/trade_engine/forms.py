from django import forms
from trade_engine.models import Balance, ActiveOrder, Trade, CancelOrder, TradeHistory, Ticker


class BalanceForm(forms.ModelForm):

    class Meta:
        model = Balance
        exclude = ["user"]


class ActiveOrderForm(forms.ModelForm):

    class Meta:
        model = ActiveOrder
        exclude = ["user"]



class TradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        exclude = ["user"]


class CancelOrderForm(forms.ModelForm):

    class Meta:
        model = CancelOrder
        exclude = ["user"]


class TradeHistoryForm(forms.ModelForm):

    class Meta:
        model = TradeHistory
        exclude = ["user"]


