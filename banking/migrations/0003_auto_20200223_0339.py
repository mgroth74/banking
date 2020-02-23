# Generated by Django 3.0.3 on 2020-02-23 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_accounts_cash_forecast_transactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cash_forecast',
            old_name='name',
            new_name='Account',
        ),
        migrations.RenameField(
            model_name='cash_forecast',
            old_name='amount',
            new_name='Amount',
        ),
        migrations.RenameField(
            model_name='cash_forecast',
            old_name='cname',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='cash_forecast',
            old_name='howoften',
            new_name='Occurrence',
        ),
        migrations.RenameField(
            model_name='cash_forecast',
            old_name='start_dt',
            new_name='Start_Dt',
        ),
    ]
