from django import forms
from trade_engine.models import WithdrawCoin, Balance, ActiveOrder, ActiveOrderTicker, Trade, CancelOrder, TradeHistory, TransHistory


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

    def __init__(self, *args, **kwargs):
        super(CancelOrderForm, self).__init__(*args, **kwargs)
        self.fields['order_id'] = forms.ChoiceField(choices=[(i, i) for i in ActiveOrderTicker.objects.all()[ActiveOrderTicker.objects.count()-1].split_json])


class TradeHistoryForm(forms.ModelForm):

    class Meta:
        model = TradeHistory
        exclude = ["user"]


class TransHistoryForm(forms.ModelForm):

    class Meta:
        model = TransHistory
        exclude = ["user"]


class WithdrawForm(forms.ModelForm):

    class Meta:
        model = WithdrawCoin
        exclude = ["user"]
