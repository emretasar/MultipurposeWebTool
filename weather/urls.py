from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather_page'),
    path('delete/<int:pk>/', views.delete_location, name="delete_weather"),
]
