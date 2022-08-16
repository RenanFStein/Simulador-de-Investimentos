from django.contrib import admin
from .models import *




class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
admin.site.register(Owner, OwnerAdmin)


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'created', 'rendimentos')   
admin.site.register(Investment, InvestmentAdmin)
