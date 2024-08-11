from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='budget_page'),
    # Add other URL patterns here
]
