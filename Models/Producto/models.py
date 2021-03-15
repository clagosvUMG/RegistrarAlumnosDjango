from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=75)
    marca = models.CharField(max_length=75)
    categoria = models.CharField(max_length=12)
    fecha_vencimiento = models.DateField()
    codigo = models.IntegerField()


class Marca(models.Model):
    nombre = models.CharField(max_length=75)
    marca = models.CharField(max_length=75)
    categoria = models.CharField(max_length=12)
    fecha_vencimiento = models.DateField()
    codigo = models.IntegerField()


class Categoria(models.Model):
    nombre = models.CharField(max_length=75)
    marca = models.CharField(max_length=75)
    categoria = models.CharField(max_length=12)
    fecha_vencimiento = models.DateField()
    codigo = models.IntegerField()
