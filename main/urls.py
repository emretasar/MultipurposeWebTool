from django.urls import path
from . import views
from register import views as register_views

urlpatterns = [
    path('', views.welcome, name=''),
    path('home/', views.home, name='home_page'),
    path('login/', register_views.login, name='login_page'),
    path('register/', register_views.register, name='register_page'),
    path('welcome/', views.welcome, name='welcome'),
]
