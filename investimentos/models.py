import re
from tabnanny import verbose
from django.db import models
from datetime import datetime


class Owner(models.Model):
    
    name = models.CharField(verbose_name="Nome", max_length=255,  null=False, blank=False)      
   
    def __str__(self):         
        return self.name
    
    class Meta:
        verbose_name = "Investidor"
        verbose_name_plural = "Investidores"  


class Investment(models.Model):
    BANK_CHOICES = (
        ("1", "Banco do Brasil"),
        ("2", "Caixa Econômica Federal"),
        ("3", "Banco Itau"),
        ("4", "Banco Bradesco"),
        ("5", "Banco Santander"),
        ("6", "Banco BTG"),
        ("7", "Banco Inter"),
        ("8", "XP Investimentos"),
        
    )
    owner = models.ForeignKey(Owner, verbose_name="Nome Investidor", on_delete=models.CASCADE, null=False, blank=False)
    bank = models.CharField(max_length=1,verbose_name="Banco", choices=BANK_CHOICES, blank=False, null=False) 
    amount = models.PositiveIntegerField(verbose_name="Valor Investido")
    created = models.DateField(verbose_name="Data da Aplicação", blank=False, null=False)
    withdrawal_forecast = models.DateField(verbose_name="Previsão de Saque", blank=False, null=False)
    withdrawal  = models.DateField(verbose_name="Saque da Aplicação", blank=True, null=True)
    def __str__(self):
        investment = f'Investidor(a) {str(self.owner)}, aplicado em {str(self.created)} o valor de {str(self.amount)}'
        return investment
    
    class Meta:
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos" 

    def yield_investiment(self):
        data = Investment.objects.filter(id=self.id).values('amount', 'created', 'withdrawal_forecast')
        data_entry =  (str(data[0]['created']).replace('-', '/'))
        data_entry = (datetime.strptime(data_entry, "%Y/%m/%d"))
        forecast_data = (str(data[0]['withdrawal_forecast']).replace('-', '/'))
        forecast_data = (datetime.strptime(forecast_data, "%Y/%m/%d"))
       
        try:         
            
            if  (int((str(abs(data_entry - forecast_data)/30)).split()[0])) > 0: 
                
               
                yields = (float(data[0]['amount']) * (1.0052) ** (float((str(abs(data_entry - forecast_data)/30)).split()[0]))) - (float(data[0]['amount']))
              
                if (int((str(abs(data_entry - forecast_data))).split()[0])) < 360:
                
                    taxation = yields * 0.225
                    tax_percentage = "22,5%"
               
                elif (int((str(abs(data_entry - forecast_data))).split()[0])) < 720:
                   
                    taxation = yields * 0.185
                    tax_percentage = "18,5%"
                   
                else:
                  
                    taxation = yields * 0.150
                    tax_percentage = "15%"
              
                return_investment = (float(data[0]['amount']) * (1.0052) ** (float((str(abs(data_entry - forecast_data)/30)).split()[0]))) - taxation
                return {"yields":'{0:.2f}'.format(yields), 
                        "taxation":'{0:.2f}'.format(taxation), 
                        "tax_percentage": tax_percentage,
                        "saldo": '{0:.2f}'.format(return_investment)}     
        except ValueError:
            balance = 'Em Aplicação'
            return balance       

    def withdrawal_investiment(self):
        data = Investment.objects.filter(id=self.id).values('amount', 'created', 'withdrawal')
        data_entry =  (str(data[0]['created']).replace('-', '/'))     
        data_entry = (datetime.strptime(data_entry, "%Y/%m/%d"))        
        saque = (str(data[0]['withdrawal']).replace('-', '/'))
        
        try:             
            saque = (datetime.strptime(saque, "%Y/%m/%d"))
            if  (int((str(abs(data_entry - saque)/30)).split()[0])) > 0: 
                yields = (float(data[0]['amount']) * (1.0052) ** (float((str(abs(data_entry - saque)/30)).split()[0]))) - (float(data[0]['amount']))
              
                if (int((str(abs(data_entry - saque))).split()[0])) < 360:
                
                    taxation = yields * 0.225
                    tax_percentage = "22,5%"
               
                elif (int((str(abs(data_entry - saque))).split()[0])) < 720:
                   
                    taxation = yields * 0.185
                    tax_percentage = "18,5%"
                   
                else:
                  
                    taxation = yields * 0.150
                    tax_percentage = "15%"
              
                return_investment = (float(data[0]['amount']) * (1.0052) ** (float((str(abs(data_entry - saque)/30)).split()[0]))) - taxation
                return '{0:.2f}'.format(return_investment)    
      
        except ValueError:
            balance = 'Em Aplicação'
            return balance         
          
   