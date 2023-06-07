from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    second_name = models.CharField(max_length=40)
    second_last_name = models.CharField(max_length=40)
    run = models.IntegerField(null=True)
    dv_run = models.CharField(max_length=1)

class EstadoPublicacion(models.Model):
    id_estpub = models.IntegerField(db_column = 'id_estpub', primary_key= True)
    nombre_estpub = models.CharField(db_column = 'nombre_estpub', max_length = 30, blank = False, null = False)

    def _str_(self):
        return str(self.nombre_estpub)
    
class CategoriaTrabajo(models.Model):
    id_categtrabajo = models.IntegerField(db_column = 'id_categtrabajo', primary_key = True)
    nombre_categtrabajo = models.CharField(db_column = 'nombre_categtrabajo', max_length = 150, blank = False, null = False)

    def _str_(self):
        return str(self.nombre_categtrabajo)

class Material(models.Model):
    id_material = models.AutoField(db_column = 'id_material', primary_key = True)
    nombre_material = models.CharField(db_column = 'nombre_material', max_length = 80, blank = False, null = False)

    def _str_(self):
        return str(self.nombre_material)
    
class Contacto(models.Model):
    id_contacto = models.AutoField(db_column = 'id_contacto', primary_key = True)
    correo = models.CharField(db_column = 'correo', max_length = 100, blank = False, null = False)
    telefono = models.IntegerField(db_column = 'telefono', blank = False, null = False)
    descripcion = models.CharField(db_column = 'descripcion', max_length = 500, blank = False, null = False)

    def _str_(self):
        return str(self.correo + self.telefono)
