from django import forms
from trade_engine.models import Balance, Trade, CancelOrder, Ticker


class TradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        exclude = ["user"]


class CancelOrderForm(forms.ModelForm):

    class Meta:
        model = CancelOrder
        exclude = ["user"]