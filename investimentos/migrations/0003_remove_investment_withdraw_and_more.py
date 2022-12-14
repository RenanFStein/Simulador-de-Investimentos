# Generated by Django 4.0.6 on 2022-08-16 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0002_investment_withdraw_alter_investment_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='withdraw',
        ),
        migrations.AddField(
            model_name='investment',
            name='withdrawal_forecast',
            field=models.DateField(null=True, verbose_name='Previsão de Saque'),
        ),
        migrations.CreateModel(
            name='WithdrawInvestment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdraw', models.DateField(verbose_name='Data do Resgate')),
                ('investment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investimentos.investment', verbose_name='Nome Investidor')),
            ],
            options={
                'verbose_name': 'Investimento',
                'verbose_name_plural': 'Investimentos',
            },
        ),
    ]
