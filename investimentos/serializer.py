from asyncore import read
from cProfile import label
from random import choices
from django.forms import ValidationError
from rest_framework.views import exception_handler
from rest_framework import serializers
from .models import *
from datetime import date, timedelta, datetime



class OwnerSerializer(serializers.ModelSerializer):
    """ Serialização model Owner """
    
    class Meta:
        model = Owner
        fields = ['id', 'name']


class InvestmentSerializer(serializers.ModelSerializer):
    """ Serialização model Owner """
    created = serializers.DateField(format="%d/%m/%Y", label='Data da Aplicação')
    withdrawal_forecast = serializers.DateField(format="%d/%m/%Y", label='Previsão de Resgate')

    class Meta:
        model = Investment
        fields = ['id', 'owner', 'bank', 'amount', 'created', 'withdrawal_forecast', 'yield_investiment','withdrawal_investiment' , 'withdrawal']

    def validate_withdrawal_forecast(created, withdrawal_forecast):
        
        try:
            date_entry = ((str((created.initial_data)["created"])).replace('-', '/'))
            withdrawn_date = (str(withdrawal_forecast)).replace('-', '/')
            date_entry = (datetime.strptime(date_entry, "%Y/%m/%d"))
            withdrawn_date = (datetime.strptime(withdrawn_date, "%Y/%m/%d"))      
        
            if withdrawn_date < date_entry:
                raise serializers.ValidationError('Previsão de saque não pode ser menor que a Data da Aplicação') 
                
            return withdrawal_forecast
        except ValueError:                 
            return 
        
    def validate_withdrawal(created, withdrawal):
        try:        
            date_entry = ((str((created.initial_data)["created"])).replace('-', '/'))        
            date_entry = (datetime.strptime(date_entry, "%Y/%m/%d"))     
            withdrawn_date = (str(withdrawal)).replace('-', '/')        
            withdrawn_date = (datetime.strptime(withdrawn_date, "%Y/%m/%d"))
            if withdrawn_date < date_entry:
                raise serializers.ValidationError('Data de saque não pode ser menor que a data da Data da Aplicação')      
            return withdrawal            
        except ValueError:     
            return       
                 
    def validate_amount(self, amount):
        if amount == 0:
            raise serializers.ValidationError('Valor de aplicação não pode ser zero')
        if amount < 0:
            raise serializers.ValidationError('Valor de aplicação não pode ser negativo')      
        return amount