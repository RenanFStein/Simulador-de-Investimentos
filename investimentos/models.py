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
    
    owner = models.ForeignKey(Owner, verbose_name="Nome Investidor", on_delete=models.CASCADE, null=False, blank=False)
    amount = models.PositiveIntegerField(verbose_name="Valor Investido")
    created = models.DateField(verbose_name="Data da Aplicação", null=False)
    withdrawal_forecast = models.DateField(verbose_name="Previsão de Saque", null=True)
    
    def __str__(self):
        investment = f'Investidor(a) {str(self.owner)}, aplicado em {str(self.created)} o valor de {str(self.amount)}'
        return investment
    
    class Meta:
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos" 

    def rendimentos(self):
        dados = Investment.objects.filter(id=self.id).values('amount', 'created', 'withdrawal_forecast')

        entrada =  (str(dados[0]['created']).replace('-', '/'))
        
        previsao = (str(dados[0]['withdrawal_forecast']).replace('-', '/'))

        entrada = (datetime.strptime(entrada, "%Y/%m/%d"))
        previsao = (datetime.strptime(previsao, "%Y/%m/%d"))
 
        try:
            if  (int((str(abs(entrada - previsao)/30)).split()[0])) > 0: 

                rendimento = (float(dados[0]['amount']) * (1.0052) ** (float((str(abs(entrada - previsao)/30)).split()[0]))) - (float(dados[0]['amount']))
              
                if (int((str(abs(entrada - previsao))).split()[0])) < 360:
                
                    tributacao = rendimento * 0.225
                    percentual = "22,5%"
               
                elif (int((str(abs(entrada - previsao))).split()[0])) < 720:
                   
                    tributacao = rendimento * 0.185
                    percentual = "18,5%"
                   
                else:
                  
                    tributacao = rendimento * 0.150
                    percentual = "15%"
              
                retorno = (float(dados[0]['amount']) * (1.0052) ** (float((str(abs(entrada - previsao)/30)).split()[0]))) - tributacao
                return {"rendimento":'{0:.2f}'.format(rendimento), 
                        "tributacao":'{0:.2f}'.format(tributacao), 
                        "percentual": percentual,
                        "saldo": '{0:.2f}'.format(retorno)}     
        except:            
            return  
           
class WithdrawInvestment(models.Model):
    investment = models.ForeignKey(Investment, verbose_name="Investimento", on_delete=models.CASCADE, null=False, blank=False)
    amount_withdraw = models.PositiveIntegerField(verbose_name="Valor Investido")
    withdraw = models.DateField(verbose_name="Data do Resgate", null=False)

    def __str__(self):
        dados = f"Retirada em {self.withdraw}"
        return dados
    
    class Meta:
        verbose_name = "Resgate Investimento"
        verbose_name_plural = "Resgate Investimentos"    

    def withdraw_investment(self): 
        print('Bem vindo')
        print(self.withdraw)
        dados = Investment.objects.get(id=self.investment_id)
        dados.withdrawal_forecast = self.withdraw
        dados.save()        
        return 
    
    def amount(self): 
        dados = Investment.objects.filter(id=self.investment_id).values('amount', 'created', 'withdrawal_forecast')
        entrada =  (str(dados[0]['created']).replace('-', '/'))        
        previsao = (str(dados[0]['withdrawal_forecast']).replace('-', '/'))
        entrada = (datetime.strptime(entrada, "%Y/%m/%d"))
        previsao = (datetime.strptime(previsao, "%Y/%m/%d")) 
        try:
            if  (int((str(abs(entrada - previsao)/30)).split()[0])) > 0: 

                rendimento = (float(dados[0]['amount']) * (1.0052) ** (float((str(abs(entrada - previsao)/30)).split()[0]))) - (float(dados[0]['amount']))
              
                if (int((str(abs(entrada - previsao))).split()[0])) < 360:
                
                    tributacao = rendimento * 0.225
                    percentual = "22,5%"
               
                elif (int((str(abs(entrada - previsao))).split()[0])) < 720:
                   
                    tributacao = rendimento * 0.185
                    percentual = "18,5%"
                   
                else:
                  
                    tributacao = rendimento * 0.150
                    percentual = "15%"
              
                self.amount_withdraw = (float(dados[0]['amount']) * (1.0052) ** (float((str(abs(entrada - previsao)/30)).split()[0]))) - tributacao
                return '{0:.2f}'.format(self.amount_withdraw)
        except:            
              
            return 