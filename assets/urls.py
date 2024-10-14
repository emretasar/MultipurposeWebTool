from django.urls import path
from . import views
from .views import currency_asset_view


urlpatterns = [
    path('', views.index, name='assets_page'),
    path('currency/', currency_asset_view, name='currency_asset_view'),
]
