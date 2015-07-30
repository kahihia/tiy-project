"""bitcoin_trade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
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
