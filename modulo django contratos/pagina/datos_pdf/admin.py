from django.contrib import admin
from .models import Contrato,Campain,Table_campain,Payment
# Register your models here.



class ContratoAdmin(admin.ModelAdmin):
    list_display= ["nombre_del_contrato", "nombre_de_la_empresa", "fecha"]
    search_fields= ["nombre_de_la_empresa"]
    list_filter= ["fecha", "nombre_del_contrato"]
    list_per_page: 10

class CampainAdmin(admin.ModelAdmin):
    search_fields= ["event"]
    list_filter= ["event", "budget"]
    list_per_page: 10

class tableCampainAdmin(admin.ModelAdmin):
    list_display= ["domain", "product", "country"]
    search_fields= ["domain"]
    list_filter= ["product", "services"]
    list_per_page: 15

class paymentAdmin(admin.ModelAdmin):
    list_display= ["company_name", "pais"]
    search_fields= ["company_name"]
    list_filter= ["pais", "type"]
    list_per_page: 15


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Campain, CampainAdmin)
admin.site.register(Table_campain, tableCampainAdmin)
admin.site.register(Payment, paymentAdmin)