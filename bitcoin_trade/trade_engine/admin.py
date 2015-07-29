from django.contrib import admin
from trade_engine.models import UserProfile, Balance, Trade, CancelOrder, Ticker

admin.site.register(UserProfile)
admin.site.register(Balance)
admin.site.register(Trade)
admin.site.register(CancelOrder)
admin.site.register(Ticker)