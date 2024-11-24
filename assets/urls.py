from django.urls import path
from . import views
from .views import currency_asset_view
from .views import currency_line_chart


urlpatterns = [
    path('', views.currency_asset_view, name='assets_page'),
	path('update_asset/<str:pk>/', views.update_entry, name="update_asset_entry"),
	path('delete_asset/<str:pk>/', views.delete_entry, name="delete_asset_entry"),
    path('chart/<str:currency_type>/', currency_line_chart, name='currency_line_chart')
]
