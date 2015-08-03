from django.contrib import admin
from trade_engine.models import UserAccount, Balance, Trade, CancelOrder, Ticker, Depth

admin.site.register(UserAccount)
admin.site.register(Balance)
admin.site.register(Trade)
admin.site.register(CancelOrder)
admin.site.register(Ticker)
admin.site.register(Depth)