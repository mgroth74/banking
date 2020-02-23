from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_list),
    path('accounts/', views.account_list, name = 'account_list'),
    path('accounts/<int:id>', views.account_detail, name = 'account_detail'),
    path('accounts/new', views.account_create, name = 'account_create'),
    path('accounts/<int:id>/edit', views.account_update, name = 'account_update'),
    path('accounts/<int:id>/delete', views.account_delete, name = 'account_delete'),
    path('transactions/', views.transaction_list, name = 'transaction_list'),
    path('transactions/<int:id>', views.transaction_detail, name = 'transaction_detail'),
    path('transactions/new', views.transaction_create, name = 'transaction_create'),
    path('transactions/<int:id>/edit', views.transaction_update, name = 'transaction_edit'),
    path('transactions/<int:id>/delete', views.transaction_delete, name = 'transaction_delete'),
    path('cash_forecast/', views.cash_forecast, name = 'cash_forecast'),
    path('cash_forecast/income/', views.income_create, name = 'income_create'),
 
]