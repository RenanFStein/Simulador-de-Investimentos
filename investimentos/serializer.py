from asyncore import read
from cProfile import label
from django.forms import ValidationError
from rest_framework.views import exception_handler
from rest_framework import serializers
from .models import *
from datetime import date, timedelta, datetime



class OwnerSerializer(serializers.ModelSerializer):
    """ Serialização do model Owner """
    
    class Meta:
        model = Owner
        fields = ['id', 'name']


class InvestmentSerializer(serializers.ModelSerializer):
    """ Serialização do model Owner """
    created = serializers.DateField(format="%d/%m/%Y", label='Data da Aplicação')
    withdrawal_forecast = serializers.DateField(format="%d/%m/%Y", label='Data do Resgate')
    
    class Meta:
        model = Investment
        fields = ['id', 'owner', 'amount', 'created', 'withdrawal_forecast', 'rendimentos','retirada' , 'withdrawal']

    def validate_withdrawal_forecast(created, withdrawal_forecast):
        entrada = ((str((created.initial_data)["created"])).replace('-', '/'))
        retirada = (str(withdrawal_forecast)).replace('-', '/')
        entrada = (datetime.strptime(entrada, "%Y/%m/%d"))
        retirada = (datetime.strptime(retirada, "%Y/%m/%d"))
        if retirada < entrada:
            raise serializers.ValidationError('Previsão de saque não pode ser menor que a Data da Aplicação')      
        return withdrawal_forecast

    def validate_withdrawal(created, withdrawal):
    
        entrada = ((str((created.initial_data)["created"])).replace('-', '/'))
        print(entrada)
        entrada = (datetime.strptime(entrada, "%Y/%m/%d"))
        print(entrada)
        try:
            retirada = (str(withdrawal)).replace('-', '/')
        
            retirada = (datetime.strptime(retirada, "%Y/%m/%d"))
            if retirada < entrada:
                raise serializers.ValidationError('Data de saque não pode ser menor que a data da Data da Aplicação')      
            return withdrawal
        except ValueError:            
            return     
        

  