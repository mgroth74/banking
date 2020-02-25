# Project Overview


## Project Description

Create a banking / cash flow application.  This application would allow a user to add accounts.  While adding an account yopu can add the account transactions in a CSV file.  Once the account is added it will present the user with a list of account, the account balances and a link to the account transactions.  A user will also be able to create a cashflow.  You would see the beginning balance and the ending balance.  You would be able to add future income and bills so you can forecast what your cashflow will be in the future.

## Project Links

- [Repo: https://github.com/mgroth74/banking]()
- [Heroku: https://mymazumaapp.herokuapp.com/]()

## Wireframes

Wireframes and user stories are located in the planning folder.




### MVP/PostMVP - 5min

MVP:
The site visitor will be able to:
- Add, update and delete an Account
-	Add, edit and delete cash flow items

Post MVP:
The site visitor will be able to:
 - Import a CSV file with account transactions
 - see the account transactions
 - Create a user account
 

## Components
##### Writing out your components and its descriptions isn't a required part of the proposal but can be helpful.

An application with three database models.
 -  Accounts: This model would be used to store the account information
 -  Transactions: This model would store the account transactions for all of the accounts
 -  Cash_Forecast: This is where the account individual cash transactions to determine the cashflow.

## Additional Libraries

Here are the dependencies:
appnope==0.1.0
asgiref==3.2.3
backcall==0.1.0
decorator==4.4.1
dj-database-url==0.5.0
Django==3.0.3
django-extensions==2.2.8
django-heroku==0.3.1
django-mathfilters==1.0.0
gunicorn==20.0.4
ipython==7.12.0
ipython-genutils==0.2.0
jedi==0.16.0
parso==0.6.1
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.3
psycopg2==2.8.4
psycopg2-binary==2.8.4
ptyprocess==0.6.0
Pygments==2.5.2
pytz==2019.3
six==1.14.0
sqlparse==0.3.0
traitlets==4.3.3
wcwidth==0.1.8
whitenoise==5.0.1


## Code Snippet

      def cash_forecast(request):
          cash_forecast = Cash_Forecast.objects.all().order_by('Start_Dt')
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


 