from ast import Delete
from django.db import models

# Create your models here.
class Jugadores(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    numero_playera = models.IntegerField(null=True,blank=True,verbose_name="Numero de playera")
    edad = models.IntegerField(null=True,blank=True,verbose_name="Edad")
    equipo=models.CharField(max_length=50,verbose_name="Equipo")
    posicion=models.CharField(max_length=50,verbose_name="Posicion")
    estadio=models.CharField(max_length=50,verbose_name="Estadio")

    def __str__(self):
        fila= "Nombre: "+self.nombre+" Equipo: "+self.equipo+" Posicion: "+self.posicion
        return fila
    
  