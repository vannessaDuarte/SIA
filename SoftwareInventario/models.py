from django.db import models

# Create your models here.
class Administrador (models.Model):


    Nombre = models.CharField(max_length=50,null=False,blank=False)
    rut = models.CharField(max_length=12,null=False,blank=False,primary_key=True)
    edad = models.IntegerField(null=False,blank=True)
    telefono = models.CharField(max_length=12,null=False,blank=False)

class Trabajador (models.Model):
        Nombre = models.CharField(max_length=50,null=False, blank=False)
        rut = models.CharField(max_length=12,null=False,blank=False,primary_key=True)
        edad = models.CharField(max_length=10,null=False,blank=False)
        telefono = models.CharField(max_length=12,null=False,blank=False)


class Inventario (models.Model):
    Nombre_de_producto = models.CharField(max_length=50,null=False,blank=False)
    Cantidad_de_producto= models.CharField(max_length=100,null=False,blank=False)
    Precio_costo= models.CharField(max_length=100,null=False,blank=False)
    Precio_venta= models.CharField(max_length=100,null=False,blank=False)
    codigo = models.CharField(max_length=50,null=False,blank=False,primary_key=True)

class Reporte_de_Inventario (models.Model):
    Productos = models.CharField(max_length=50,null=False,blank=False)
    Precio_costo= models.CharField(max_length=100,null=False,blank=False)
    Precio_venta= models.CharField(max_length=100,null=False,blank=False)
    codigo = models.CharField(max_length=50,null=False,blank=False,primary_key=True)

class Cotizaciones(models.Model):
    Fecha_de_emision = models.CharField(max_length=50,null=False,blank=False,primary_key=True)
    Precio_costo = models.CharField(max_length=100,null=False,blank=False)
    Precio_venta = models.CharField(max_length=100,null=False,blank=False)
