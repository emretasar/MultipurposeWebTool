from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_entries, name='budget_entries_page'),
	path('update_budget/<str:pk>/', views.update_entry, name="update_budget_entry"),
	path('delete_budget/<str:pk>/', views.delete_entry, name="delete_budget_entry"),
]
