from django.contrib import admin
from .models import PaymentAddress
# Register your models here.
class PaymentAddressAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile_number']
    
admin.site.register(PaymentAddress,PaymentAddressAdmin)