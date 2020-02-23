from django.db import models

class Accounts(models.Model):
  name = models.CharField(default='', max_length=200)
  acct_type = models.CharField(default='', max_length=20)
  owner = models.CharField(default='', max_length=100)
  dt_opened = models.DateField(auto_now=False, auto_now_add=True) 
  interest_rt = models.CharField(default='0', max_length=100)
  
  def __str__(self):
    return self.name

class Transactions(models.Model):
  date = models.DateField(auto_now=False, auto_now_add=True) 
  description = models.CharField(default = '', max_length= 400)
  amount = models.DecimalField(max_digits=40, decimal_places=2)
  balance = models.IntegerField(default = '0')
  prevbalance = models.IntegerField(default = '0')
  name = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = 'transactions')
  
  def __str__(self):
    return self.description

class Cash_Forecast(models.Model):
  entry_type = (
      ('I','Income'),
      ('B', 'Bill'),
      )
  Name = models.CharField(default='', max_length=200)
  Entry_Type = models.CharField(max_length=1, choices=entry_type)
  Amount = models.DecimalField(max_digits=40, decimal_places=2)
  Occurrence = models.CharField(default='', max_length=200)
  Start_Dt = models.DateField(auto_now=False, auto_now_add=False) 
  Account = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = 'Cashforecast')

  def __str__(self):
    return self.cname

