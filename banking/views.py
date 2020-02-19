from django.shortcuts import render, redirect
from .models import Accounts, Transactions
from .forms import AccountForm, TransactionForm


def account_list(request):
    account = Accounts.objects.all()
    return render(request, 'account_list.html', {'account': account})

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



def transaction_list(request):
    transaction = Transactions.objects.all()
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


# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid:
#             # transaction = transaction.objects.get(id=id)
#             transaction.img_url = form.cleaned_data['image']
#             transaction=form.save()
#             # return redirect('transaction_detail', id = transaction.id)
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')
