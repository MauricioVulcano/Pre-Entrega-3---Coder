from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class listaJuegos(models.Model):
    consola = models.CharField(max_length=30)
    juego = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    
class listaPerifericos(models.Model):
    consola = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)

