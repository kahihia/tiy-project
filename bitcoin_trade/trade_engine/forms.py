from django import forms
from trade_engine.models import Balance, Trade, CancelOrder, Ticker


class BalanceForm(forms.ModelForm):

    class Meta:
        model = Balance
        exclude = ["user"]


class TradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        exclude = ["user"]


class CancelOrderForm(forms.ModelForm):

    class Meta:
        model = CancelOrder
        exclude = ["user"]