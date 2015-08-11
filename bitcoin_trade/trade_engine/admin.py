from django.contrib import admin
from trade_engine.models import UserAccount, DepositAddress, ActiveOrder, ActiveOrderTicker, Balance, BalanceTicker, Trade, TradeTicker, CancelOrder, CancelOrderTicker, TradeHistory, TradeHistoryTicker, TransHistory, TransHistoryTicker, Ticker, Depth

admin.site.register(UserAccount)
admin.site.register(DepositAddress)
admin.site.register(Balance)
admin.site.register(BalanceTicker)
admin.site.register(ActiveOrder)
admin.site.register(ActiveOrderTicker)
admin.site.register(Trade)
admin.site.register(TradeTicker)
admin.site.register(CancelOrder)
admin.site.register(CancelOrderTicker)
admin.site.register(TradeHistory)
admin.site.register(TradeHistoryTicker)
admin.site.register(TransHistory)
admin.site.register(TransHistoryTicker)
admin.site.register(Ticker)
admin.site.register(Depth)