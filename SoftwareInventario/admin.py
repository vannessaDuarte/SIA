from django.contrib import admin
from SoftwareInventario.models import *
# Register your models here.
admin.site.register(Administrador)
admin.site.register(Trabajador)
admin.site.register(Inventario)
admin.site.register(Reporte_de_Inventario)
admin.site.register(Cotizaciones)
