from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    rut = models.IntegerField(db_column = 'rut', null=False, blank=False, unique=True)
    dvrut = models.CharField(db_column = 'dvrut', null=False, blank=False, max_length=1)
    second_name = models.CharField(db_column = 'second_name', max_length=40, null=True, blank=True)
    second_last_name = models.CharField(db_column = 'second_last_name', max_length=40, null=True, blank=True)
    phone_number = models.IntegerField(db_column = 'phone_number', null=False, blank=False)

    groups = models.ManyToManyField(
    'auth.Group',
    related_name='custom_groups',
    blank=True,
    help_text='The groups this user belongs to. A user will get all permissions '
              'granted to each of their groups.',
    verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

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