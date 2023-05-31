from django.db import models

# Create your models here.
class EstadoPublicacion(models.Model):
    id_estpub = models.IntegerField(db_column = 'id_estpub', primary_key= True)
    nombre_estpub = models.CharField(db_column = 'nombre_estpub', max_length = 30, blank = False, null = False)

    def _str_(self):
        return str(self.nombre_estpub)