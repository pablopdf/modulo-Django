from distutils.command.upload import upload
from operator import mod
from django.db import models

# Create your models here.

class Contrato(models.Model):
    nombre_del_contrato = models.CharField(max_length=30)
    nombre_de_la_empresa = models.CharField(max_length=70)
    contacto = models.CharField(max_length=120)
    contacto_alt = models.CharField(max_length=120)
    ref_finanzas = models.IntegerField()
    direccion = models.CharField(max_length=200)
    ciudad_pais = models.CharField(max_length=200)
    email = models.EmailField()
    tel = models.IntegerField()
    tax_id = models.IntegerField()
    fecha = models.DateField()
    contenido_del_contrato = models.TextField()

    def __str__(self):
        return self.nombre_del_contrato


class Campain(models.Model):
    representante= models.CharField(max_length=150)
    budget = models.IntegerField()
    geos = models.CharField(max_length=170)
    cpa = models.IntegerField()
    event = models.CharField(max_length=70)
    test_t = models.IntegerField()

    def __str__(self):
        return self.representante

class Table_campain(models.Model):
    domain = models.URLField()
    product = models.CharField(max_length=200)
    country = models.CharField(max_length=80)
    cpm = models.CharField(max_length=80)
    services = models.CharField(max_length=200)
    deal = models.CharField(max_length=300)
    implementation = models.CharField(max_length=70)

    def __str__(self):
        return self.domain

class Payment(models.Model):
    company_name = models.CharField(max_length=70)
    city = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    cp = models.CharField(max_length=30)
    bank = models.CharField(max_length=250)
    swift = models.CharField(max_length=250)
    aba = models.IntegerField()
    routing = models.IntegerField()
    cbu = models.IntegerField()
    other = models.TextField()
    account = models.IntegerField()
    type = models.CharField(max_length=80)
    currency = models.IntegerField()
    paypal = models.IntegerField()


    def __str__(self):
        return self.company_name

