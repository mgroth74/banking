# Generated by Django 3.0.3 on 2020-02-21 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0006_accounts_beg_bal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashforecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=200)),
                ('amount', models.IntegerField(default='0', max_length=100)),
                ('howoften', models.CharField(default='', max_length=200)),
                ('start_dt', models.DateTimeField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cashforecast', to='banking.Accounts')),
            ],
        ),
    ]
