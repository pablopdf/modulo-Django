import imp
from django.urls import path
from pagina.views import contrato2

urlpatterns = [
    path('prueba/', contrato2),
]