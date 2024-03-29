from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models import ImageField

# Create your models here.
class User(AbstractUser):
    second_name = models.CharField(max_length=40, null=True)
    second_last_name = models.CharField(max_length=40, null=True)
    run = models.IntegerField(null=True)
    dv_run = models.CharField(max_length=1)
    phone = models.IntegerField(null=True)
    groups = models.ManyToManyField(Group,blank=True, related_name='user_groups')

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

class EstadoPublicacion(models.Model):
    id_estpub = models.IntegerField(db_column = 'id_estpub', primary_key= True)
    nombre_estpub = models.CharField(db_column = 'nombre_estpub', max_length = 30, blank = False, null = False)

    def __str__(self):
        return str(self.nombre_estpub)
    
class CategoriaTrabajo(models.Model):
    id_categtrabajo = models.IntegerField(db_column = 'id_categtrabajo', primary_key = True)
    nombre_categtrabajo = models.CharField(db_column = 'nombre_categtrabajo', max_length = 150, blank = False, null = False)

    def __str__(self):
        return str(self.nombre_categtrabajo)

class Material(models.Model):
    id_material = models.AutoField(db_column = 'id_material', primary_key = True)
    nombre_material = models.CharField(db_column = 'nombre_material', max_length = 80, blank = False, null = False)

    def __str__(self):
        return str(self.nombre_material)
    
class Contacto(models.Model):
    id_contacto = models.AutoField(db_column = 'id_contacto', primary_key = True)
    correo = models.CharField(db_column = 'correo', max_length = 100, blank = False, null = False)
    telefono = models.IntegerField(db_column = 'telefono', blank = False, null = False)
    descripcion = models.CharField(db_column = 'descripcion', max_length = 500, blank = False, null = False)

    def __str__(self):
        return str(self.correo + self.telefono)
    
class Publicacion(models.Model):
    id_publicacion = models.AutoField(db_column = 'id_publicacion', primary_key = True)
    titulo_publicacion = models.CharField(db_column = 'titulo_publicacion', max_length = 80, null=False, blank=False)
    diagnostico_publicacion = models.CharField(db_column = 'diagnostico_publicacion', max_length = 500, null=False, blank=False)
    fecha_publicacion = models.DateField(db_column='fecha_publicacion', null=False, blank=False)
    descripcion_publicacion = models.CharField(db_column = 'descripcion_publicacion', max_length = 1000, null=False, blank=False)
    foto1 = models.ImageField(upload_to='foto_publicacion/', null=False, blank=False)
    foto2 = models.ImageField(upload_to='foto_publicacion/', null=True, blank=True)
    foto3 = models.ImageField(upload_to='foto_publicacion/', null=True, blank=True)
    foto4 = models.ImageField(upload_to='foto_publicacion/', null=True, blank=True)
    foto5 = models.ImageField(upload_to='foto_publicacion/', null=True, blank=True)
    foto6 = models.ImageField(upload_to='foto_publicacion/', null=True, blank=True)
    fecha_revision = models.DateTimeField(db_column='fecha_revision', null=True, blank=True)
    cant_rechaz = models.IntegerField(db_column = 'cantidad_rechazos', blank = False, null = False)
    motivo_rechazo = models.CharField(db_column = 'motivo_rechazo', max_length = 500, null=True, blank=True)
    id_categoria = models.ForeignKey(CategoriaTrabajo, db_column='id_categoria', on_delete=models.CASCADE)
    id_estpub = models.ForeignKey(EstadoPublicacion, db_column='id_estpub', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, db_column='id_user', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo_publicacion} {self.id_user.username} {self.id_categoria.nombre_categtrabajo} {self.id_estpub.nombre_estpub}"
    
    def get_image_fields(self):
        fields = []
        for field in self._meta.fields:
            if isinstance(field, ImageField):
                fields.append(field)
        return fields

class PublicacionMaterial(models.Model):
    id_publicacion = models.ForeignKey('Publicacion',on_delete=models.CASCADE)
    id_material = models.ForeignKey('Material',on_delete=models.CASCADE)

    def __str__(self):
        msn = f"{self.id_publicacion} {self.id_material}"
        return str(msn)

class Solicitud(models.Model):
    id_solicitud = models.AutoField(db_column='id_solicitud', primary_key=True)
    fecha_solicitud = models.DateField(db_column='fecha_solicitud', null=False, blank=False)
    descripcion_solicitud = models.CharField(db_column='descripcion_solicitud', null=False, blank=False, max_length=500)
    id_user = models.ForeignKey(User, db_column='id_user', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha_solicitud + " " + self.descripcion_solicitud)