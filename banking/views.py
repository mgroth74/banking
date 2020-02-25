from django.shortcuts import render, redirect
from .models import Accounts, Transactions, Cash_Forecast
from .forms import AccountForm, TransactionForm, Cash_ForecastForm
from django.db.models import Sum
import csv, io
from django.contrib import messages



def account_list(request):
    account = Accounts.objects.all()
    balance = Accounts.objects.raw(""" SELECT banking_accounts.id, 
                banking_accounts.name, 
                banking_transactions.balance, 
                banking_accounts.interest_rt 
        FROM banking_transactions 
                JOIN banking_accounts on banking_transactions.name_id = banking_accounts.id 
            WHERE banking_transactions.id in 
                (SELECT distinct max(banking_transactions.id) 
                    FROM banking_transactions group by banking_transactions.name_id) """)

    return render(request, 'account_list.html',
            {'account': account,
             'balance': balance,})

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
    transaction = Transactions.objects.all().order_by('id').reverse()
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
    balance = Accounts.objects.raw(""" SELECT banking_accounts.id, 
            banking_accounts.name, 
            banking_transactions.balance, 
            banking_transactions.id, 
            banking_accounts.interest_rt 
    FROM banking_transactions 
            JOIN banking_accounts on banking_transactions.name_id = banking_accounts.id 
        WHERE banking_transactions.id in 
            (SELECT distinct max(banking_transactions.id) 
                FROM banking_transactions WHERE banking_transactions.name_id = 4) """)

    # income2 = Cash_Forecast.objects.raw(""" Select sum(banking_cash_forecast."Amount") 
    #                             from banking_cash_forecast where banking_cash_forecast."Entry_Type" = 'B' """)

    income = Cash_Forecast.objects.filter(Entry_Type="I").aggregate(Sum('Amount'))
    bill = Cash_Forecast.objects.filter(Entry_Type="B").aggregate(Sum('Amount'))
    cash = income.get('Amount__sum') - bill.get('Amount__sum')
    # total = balance.get('Amount') + cash

#     suma = Contrato.objects.aggregate(Sum('lote__Costo'))
# decimal_val = float(suma['lote__Costo__sum'])
                
    return render(request, 'cash_forecast.html', 
                {'cash_forecast': cash_forecast, 
                'balance' : balance,
                'income' : income,
                'bill' : bill,
                'cash' : cash,
                
                })


def cash_forecast_create(request):
    if request.method == 'POST':
        form = Fash_ForecastForm(request.POST)
        if form.is_valid:
            income = form.save()
            return redirect('cash_forecast')
    else:
        form = Cash_ForecastForm()
        return render(request, 'cash_forecast_form.html', {'form': form})



def transaction_upload(request):
    template = "transaction_upload.html"

    prompt = {
        'order': 'Order of the CSV should be:  date, description, amount, balance, prevbalance, account'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    # if not csv_file.name.endwith('.csv'):
    #     message.err(request, 'Invalid file type')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Transactions.objects.update_or_create(
            date=column[0],
            description=column[1],
            amount=column[2],
            balance=column[3],
            prevbalance=column[4],
            name_id=column[5],
        )
   
    return render(request, template)

def cash_forecast_update(request, id):
    cash_forecast = Cash_Forecast.objects.get(id = id)
    if request.method == 'POST':
        form = Cash_ForecastForm(request.POST, instance = cash_forecast)
        if form.is_valid:
            seller = form.save()
            return redirect('cash_forecast', id = cash_forecast.id)
    else:
        form = Cash_ForecastForm(instance = cash_forecast)
        return render(request, 'cash_forecast_form.html', {'form': form})

def cash_forecast_delete(request, id):
    Cash_Forecast.objects.get(id = id).delete()
    return redirect('cash_forecast')


