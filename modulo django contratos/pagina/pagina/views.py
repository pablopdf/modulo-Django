import imp
from multiprocessing import context
from django.http import HttpResponse

from django.views.generic import View

from django.template.loader import get_template

from .utils import render_to_pdf

from datos_pdf.models import Contrato,Campain,Table_campain,Payment

from django.shortcuts import render



class GeneradorDePDF(View):
    def get(self, *args, **kwargs):       
        contracts = Contrato.objects.get(id=1)
        context = {
            "Contrato":contracts.nombre_del_contrato,
            "empresa": contracts.nombre_de_la_empresa,
            "Fecha": contracts.fecha,
            "contenido_del_contrato": contracts.contenido_del_contrato,
        }

        pdf = render_to_pdf('contrato.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "%s.pdf" %("Nombre del contrato")
            content = "inline; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("No encontrado")

def contrato2(request):
    contracts = Contrato.objects.all()
    data= {
        'contrato':contracts
    }
    return render(request, 'full contracts/contracts2.html', data)

def prueba_template(request):
    contracts = Contrato.objects.get(id=1)    
    campainData = Campain.objects.get(id=1)
    tableCampainData = Table_campain.objects.get(id=1)
    paymentData = Payment.objects.get(id=1)
    context = {
            "nombre_de_la_empresa":contracts.nombre_de_la_empresa,
            "contract": contracts.nombre_del_contrato,
            "date": contracts.fecha,
            "direccion": contracts.direccion,
            "budget":campainData.budget,
            "geos":campainData.geos,
            "cpa":campainData.cpa,
            "event":campainData.event,
            "test_t":campainData.test_t,
            "representante":campainData.representante,
            "domain":tableCampainData.domain,
            "product":tableCampainData.product,
            "country":tableCampainData.country,
            "cpm":tableCampainData.cpm,
            "services":tableCampainData.services,
            "deal":tableCampainData.deal,
            "contacto":contracts.contacto,
            "contacto_alt":contracts.contacto_alt,
            "ref_finanzas":contracts.ref_finanzas,
            "ciudad_pais":contracts.ciudad_pais,
            "email":contracts.email,
            "tel":contracts.tel,
            "tax_id":contracts.tax_id,
            "implementation":tableCampainData.implementation,
            "company_name":paymentData.company_name,
            "city":paymentData.city,
            "cp":paymentData.cp,
            "pais":paymentData.pais,
            "bank":paymentData.bank,
            "swift":paymentData.swift,
            "aba":paymentData.aba,
            "routing":paymentData.routing,
            "cbu":paymentData.cbu,
            "other":paymentData.other,
            "account":paymentData.account,
            "type":paymentData.type,
            "currency":paymentData.currency,
            "paypal":paymentData.paypal,

        }
    return render(request, 'prueba.html', context)

def checkbox(request):
    ms = ['anexo_native_esp','anexo_native_eng','io_clientes','io_hb_esp','io_hb_eng','io_hb_esp_exc','io_int','io_partner']
    if request.method == 'post':
        contratocheck = request.post.getlist('contratos')
        print(contratocheck)
        if contratocheck == ['anexo_native_esp']:
            print('selección Anexo Native Esp')
    return render(request, 'sections/checkbox.html')