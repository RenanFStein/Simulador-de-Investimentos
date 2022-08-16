from django.contrib import admin
from .models import *




class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
admin.site.register(Owner, OwnerAdmin)


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'created', "withdrawal_forecast")   
admin.site.register(Investment, InvestmentAdmin)

class WithdrawInvestmentAdmin(admin.ModelAdmin):
    list_display = ('id','withdraw')   
admin.site.register(WithdrawInvestment, WithdrawInvestmentAdmin)