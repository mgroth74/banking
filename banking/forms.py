from django import forms
from .models import Accounts, Transactions, Cash_Forecast

class AccountForm(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = ('name','acct_type', 'dt_opened', 'owner', 'interest_rt',)

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = ('description', 'amount','name',)


class Cash_ForecastForm(forms.ModelForm):

    class Meta:
        model = Cash_Forecast
        fields = ('cname', 'amount','howoften', 'start_dt', 'name',)