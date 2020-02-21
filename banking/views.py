from django.shortcuts import render, redirect
from .models import Accounts, Transactions, Cash_Forecast
from .forms import AccountForm, TransactionForm, Cash_ForecastForm


def account_list(request):
    account = Accounts.objects.raw(""" SELECT banking_accounts.id, 
                banking_accounts.name, 
                banking_transactions.balance, 
                banking_transactions.id, 
                banking_accounts.interest_rt 
        FROM banking_transactions 
                JOIN banking_accounts on banking_transactions.name_id = banking_accounts.id 
            WHERE banking_transactions.id in 
                (SELECT distinct max(banking_transactions.id) 
                    FROM banking_transactions group by banking_transactions.name_id) """)

    return render(request, 'account_list.html', {'account': account})

# def account_list(request):
#     account = Accounts.objects.all()
#     return render(request, 'account_list.html', {'account': account})

def account_detail(request, id):
    account = Accounts.objects.get(id = id)
    return render(request, 'account_detail.html', {'account': account})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid:
            account = form.save()
            return redirect('account_detail', id = account.id)
    else:
        form = AccountForm()
        return render(request, 'account_form.html', {'form': form})

def account_update(request, id):
    account = Accounts.objects.get(id = id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance = account)
        if form.is_valid:
            seller = form.save()
            return redirect('account_detail', id = account.id)
    else:
        form = AccountForm(instance = account)
        return render(request, 'account_form.html', {'form': form})

def account_delete(request, id):
    Accounts.objects.get(id = id).delete()
    return redirect('account_list')

# def account_balance(request, id):
#     balance = Transactions.objects.filter(name_id=id).values_list('balance').order_by('-id')[0:1]   
#     return reneder(reequest, 'account_list.html', {'balance': balance})




def transaction_list(request, id):
    transaction = Transactions.objects.all().order_by('id')
    return render(request, 'transaction_list.html', {'transaction': transaction})

def transaction_detail(request, id):
    transaction = Transactions.objects.get(id = id)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid:
            transaction = form.save()
            return redirect('transaction_detail', id = Transactions.id)
    else:
        form = TransactionForm()
        return render(request, 'transaction_form.html', {'form': form})

def transaction_update(request, id):
    transaction = Transactions.objects.get(id = id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance = transaction)
        if form.is_valid:
            transaction = form.save()
            return redirect('transaction_detail', id = Transaction.id)
    else:
        form = TransactionForm(instance = transaction)
        return render(request, 'transaction_form.html', {'form': form})

def transaction_delete(request, id):
    Transactions.objects.get(id = id).delete()
    return redirect('transaction_list')


def cash_forecast(request):
    cash_forecast = Cash_Forecast.objects.all().order_by('id')
    return render(request, 'cash_forecast.html', {'cash_forecast': cash_forecast})


def income_create(request):
    if request.method == 'POST':
        form = Cash_ForecastForm(request.POST)
        if form.is_valid:
            income = form.save()
            return redirect('cash_forecast')
    else:
        form = Cash_ForecastForm()
        return render(request, 'income_form.html', {'form': form})

def bill_create(request):
    if request.method == 'POST':
        form = Cash_ForecastForm(request.POST)
        if form.is_valid:
            bill = form.save()
            return redirect('cash_forecast')
    else:
        form = Cash_ForecastForm()
        return render(request, 'bill_form.html', {'form': form})