from django.contrib import admin
from .models import Accounts, Transactions, Cash_Forecast

# Register your models here.

admin.site.register(Accounts)
admin.site.register(Transactions)
admin.site.register(Cash_Forecast)