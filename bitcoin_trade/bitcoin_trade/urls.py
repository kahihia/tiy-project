from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from trade_engine.views import base, user_registration, CreateUserProfileView, UpdateUserProfileView, DeleteUserProfileView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, {'next_page': 'base'}, name='logout'),
    url(r'^registration/', user_registration, name='user_registration'),
    url(r'^create_user_profile/', CreateUserProfileView.as_view(), name='create_user_profile'),
    url(r'^update_user_profile/', UpdateUserProfileView.as_view(), name='update_user_profile'),
    url(r'^delete_user_profile/', DeleteUserProfileView.as_view(), name='delete_user_profile')
]
