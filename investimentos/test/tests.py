from urllib import response
from rest_framework.test import APITestCase
from ..models import *
from django.urls import reverse
from rest_framework import status

class InvestimentosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Investment-list')
        self.proprierario_1 = Owner.objects.create(name='Renan')        
        self.investiment_1 = Investment.objects.create(
                            owner= self.proprierario_1,
                            bank= "1",
                            amount= 1000,
                            created= "2023-10-02",
                            withdrawal_forecast= "2022-10-01",
                            #withdrawal= "" 
                            )

    def test_request_get_for_list_investment(self):
        """Testes para verificar a requisição do GET para listar os Investimentos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_for_create_investment(self):
        """Testes para verificar a requisição do POST para criar um Investimentos"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 1000,
            'created': '2021-10-02',
            'withdrawal_forecast': '2022-10-01',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # Inicio - Testes do campo Owner
    def test_request_post_owner_empty(self):
        """Testes para verificar a requisição do POST com owner vazio"""
        data = {
            'owner': '',
            'bank': '1',
            'amount': 1,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"owner":["Este campo não pode ser nulo."]}') 

    def test_request_post_owner_nonexistent_string(self):
        """Testes para verificar a requisição do POST com owner(PK) string"""
        data = {
            'owner': 'teste',
            'bank': '1',
            'amount': 1,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"owner":["Tipo incorreto. Esperado valor pk, recebeu str."]}') 

    def test_request_post_owner_nonexistent_pk(self):
        """Testes para verificar a requisição do POST com owner(PK) inexistente"""
        data = {
            'owner': '2',
            'bank': '1',
            'amount': 1,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"owner":["Pk inválido \\"2\\" - objeto não existe."]}') 
    # Fim - Testes do campo Owner

    # Inicio - Testes do campo Bank

    def test_request_post_bank_nonexistent(self):
        """Testes para verificar a requisição do POST com bank string"""
        data = {
            'owner': '1',
            'bank': 'a',
            'amount': 1,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"bank":["\\"a\\" não é um escolha válido."]}') 

    # Fim - Testes do campo Bank

    # Inicio - Testes do campo Datas

    def test_request_post_for_create_investiment_date_initial_higher_than_forecast(self):
        """Testes para verificar a requisição do POST com data de aplicação maior que previsão de resgate"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 1000,
            'created': '2023-10-02',
            'withdrawal_forecast': '2022-10-01',
        }
        response = (self.client.post(self.list_url, data=data)) 
        self.assertEquals(response.content.decode("utf-8"), 
        '{"withdrawal_forecast":["Previsão de saque não pode ser menor que a Data da Aplicação"]}')        

    def test_request_post_for_create_investiment_empty_start_date(self):
        """Testes para verificar a requisição do POST com data de aplicação vazia"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 1000,
            'created': '',
            'withdrawal_forecast': '2022-10-01',
        }
        response = (self.client.post(self.list_url, data=data)) 
        self.assertEquals(response.content.decode("utf-8"), 
        '{"created":["Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD."]}')

    def test_request_post_for_create_investiment_empty_forecast_date(self):
        """Testes para verificar a requisição do POST com data de previsão vazia"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 1000,
            'created': '2022-10-01',
            'withdrawal_forecast': '',
        }
        response = (self.client.post(self.list_url, data=data)) 
        self.assertEquals(response.content.decode("utf-8"), 
        '{"withdrawal_forecast":["Formato inválido para data. Use um dos formatos a seguir: YYYY-MM-DD."]}')

    def test_request_post_for_create_investiment_amount_string(self):
        """Testes para verificar a requisição do POST com valor STRING"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 'a',
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }
        response = (self.client.post(self.list_url, data=data)) 
        self.assertEquals(response.content.decode("utf-8"), 
        '{"amount":["Um número inteiro válido é exigido."]}')          

    def test_request_post_for_create_investiment_amount_zero(self):
        """Testes para verificar a requisição do POST com valor zerado"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 0,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"amount":["Valor de aplicação não pode ser zero"]}')        
   
    def test_request_post_for_create_investiment_amount_negative(self):
        """Testes para verificar a requisição do POST com valor negativo"""
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': -1,
            'created': '2022-10-01',
            'withdrawal_forecast': '2022-10-01',
        }        
        response = (self.client.post(self.list_url, data=data))     
        self.assertEquals(response.content.decode("utf-8"), 
            '{"amount":["Valor de aplicação não pode ser negativo"]}') 

    def test_request_delete_investment(self):
        """Testes para verificar a requisição DELETE não permitida """
        response = self.client.delete('/api/Investment/102/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_put_investment(self):
        """Testes para verificar a requisição PUT não permitida """
        data = {
            'owner': self.proprierario_1.id,
            'bank': '1',
            'amount': 50000,
            'created': '2021-10-02',
            'withdrawal_forecast': '2022-10-01',
        }
        response = self.client.put('/api/Investment/102/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)      
        