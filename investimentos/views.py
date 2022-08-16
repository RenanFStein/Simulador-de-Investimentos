from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializer import *

class OwnerViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados do Owner """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer    

class InvestmentViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados do Investment """
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer      

class WithdrawInvestmentViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados do Investment """
    queryset = WithdrawInvestment.objects.all()
    serializer_class = WithdrawInvestmentSerializer   

