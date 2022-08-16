from django.urls import path, include
from rest_framework import routers
from .views import *
from .serializer import *

router = routers.DefaultRouter()
router.register('Owner',OwnerViewSet, basename='Owner')
router.register('Investment', InvestmentViewSet, basename='Investment')
router.register('WithdrawInvestment', WithdrawInvestmentViewSet, basename='WithdrawInvestment')
urlpatterns = [
    path('api/', include(router.urls)),

]