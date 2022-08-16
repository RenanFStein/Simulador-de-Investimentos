from django.contrib import admin
from .models import *

class InvestmentInline(admin.TabularInline):
    model = Investment

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'created', "withdrawal_forecast", 'retirada', 'withdrawal')   
admin.site.register(Investment, InvestmentAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    inlines = [
        InvestmentInline, 
       ]
admin.site.register(Owner, OwnerAdmin)