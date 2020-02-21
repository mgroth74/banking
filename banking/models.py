from django.db import models

class Accounts(models.Model):
    name = models.CharField(default='', max_length=200)
    acct_type = models.CharField(default='', max_length=20)
    beg_bal = models.IntegerField(default = '0', max_length= 100)
    owner = models.CharField(default='', max_length=400)
    dt_opened = models.DateTimeField(blank=True, null=True) 
    interest_rt = models.CharField(default='0', max_length=100)
    
    def __str__(self):
      return self.name

class Transactions(models.Model):
  date = models.DateTimeField(blank=True, null=True) 
  description = models.CharField(default = '', max_length= 400)
  amount = models.IntegerField(default = '0', max_length= 100)
  balance = models.IntegerField(default = '0', max_length= 100)
  prevbalance = models.IntegerField(default = '0', max_length= 100)
  name = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = 'transactions')
  
  def __str__(self):
    return self.description

class Cash_Forecast(models.Model):
  cname = models.CharField(default='', max_length=200)
  amount = models.IntegerField(default = '0', max_length= 100)
  howoften = models.CharField(default='', max_length=200)
  start_dt = models.DateTimeField(blank=True, null=True) 
  name = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = 'Cashforecast')

