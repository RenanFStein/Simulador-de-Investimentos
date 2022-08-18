from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializer import *


class OwnerViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados Owner """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer    
    http_method_names = ['get'] 
class InvestmentViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados Investment """
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer     
    http_method_names = ['get', 'post'] 
    


 

