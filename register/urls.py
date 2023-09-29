from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login_page'),
    path('register/', views.register, name='register_page'),
]
