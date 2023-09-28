from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.welcome, name=''),
    path('', include('register.urls')),
    path('todos/', include('todo.urls')),
    path('home/', views.home, name='home_page'),
    path('welcome/', views.welcome, name='welcome'),
]
