from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from trade_engine.views import base, indicators, user_registration, account_settings, history, ticker_view, depth_view, CreateBalanceFormView, CreateActiveOrderFormView, CreateTradeFormView, CreateCancelOrderView, CreateTradeHistoryView, CreateTransHistoryView, CreateWithdrawCoinView, CreateUserAccountView, UpdateUserAccountView, DeleteUserAccountView, CreateUserAddressView, UpdateUserAddressView, DeleteUserAddressView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^indicators/', login_required(indicators), name='indicators'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', login_required(logout), {'next_page': 'base'}, name='logout'),
    url(r'^registration/', user_registration, name='user_registration'),
    url(r'^account_settings/', login_required(account_settings), name='account_settings'),
    url(r'^history/', login_required(history), name='history'),
    url(r'^get_balance/', login_required(CreateBalanceFormView.as_view()), name='get_balance_form'),
    url(r'^get_active_orders/', login_required(CreateActiveOrderFormView.as_view()), name='get_active_orders_form'),
    url(r'^get_ticker/', login_required(ticker_view), name='get_ticker'),
    url(r'^get_depth/', login_required(depth_view), name='get_depth'),
    url(r'^trade/', login_required(CreateTradeFormView.as_view()), name='create_trade_form'),
    url(r'^cancel_trade/', login_required(CreateCancelOrderView.as_view()), name='create_cancel_order_view'),
    url(r'^get_trade_history/', login_required(CreateTradeHistoryView.as_view()), name='trade_history_view'),
    url(r'^get_trans_history/', login_required(CreateTransHistoryView.as_view()), name='trans_history_view'),
    url(r'^withdraw_coin/', login_required(CreateWithdrawCoinView.as_view()), name='withdraw_coin_view'),
    url(r'^create_user_profile/', login_required(CreateUserAccountView.as_view()), name='create_user_account'),
    url(r'^update_user_profile/(?P<pk>\d+)/', login_required(UpdateUserAccountView.as_view()), name='update_user_account'),
    url(r'^delete_user_profile/(?P<pk>\d+)/', login_required(DeleteUserAccountView.as_view()), name='delete_user_account'),
    url(r'^create_user_address/', login_required(CreateUserAddressView.as_view()), name='create_user_address'),
    url(r'^update_user_address/(?P<pk>\d+)/', login_required(UpdateUserAddressView.as_view()), name='update_user_address'),
    url(r'^delete_user_address/(?P<pk>\d+)/', login_required(DeleteUserAddressView.as_view()), name='delete_user_address'),
]