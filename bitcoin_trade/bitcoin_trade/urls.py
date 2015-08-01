from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from trade_engine.views import base, user_registration, account_settings, CreateBalanceFormView, CreateActiveOrderFormView, CreateTradeFormView, CreateCancelOrderView, CreateUserAccountView, UpdateUserAccountView, DeleteUserAccountView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, {'next_page': 'base'}, name='logout'),
    url(r'^registration/', user_registration, name='user_registration'),
    url(r'^account_settings/', account_settings, name='account_settings'),
    url(r'^get_balance/', CreateBalanceFormView.as_view(), name='get_balance_form'),
    url(r'^get_active_orders/', CreateActiveOrderFormView.as_view(), name='get_active_orders_form'),
    url(r'^trade/', CreateTradeFormView.as_view(), name='create_trade_form'),
    url(r'^cancel_order/', CreateCancelOrderView.as_view(), name='create_cancel_order_view'),
    url(r'^create_user_profile/', CreateUserAccountView.as_view(), name='create_user_account'),
    url(r'^update_user_profile/(?P<pk>\d+)/', UpdateUserAccountView.as_view(), name='update_user_account'),
    url(r'^delete_user_profile/(?P<pk>\d+)/', DeleteUserAccountView.as_view(), name='delete_user_account'),
]
