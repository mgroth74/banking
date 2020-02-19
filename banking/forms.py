from django import forms
from .models import Accounts, Transactions

class AccountForm(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = ('name','acct_type', 'dt_opened', 'owner', 'interest_rt',)

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = ('description', 'amount','name',)