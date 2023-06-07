from django.contrib import admin
from .models import User,EstadoPublicacion,CategoriaTrabajo,Material,Contacto

# Register your models here.
admin.site.register(User)
admin.site.register(EstadoPublicacion)
admin.site.register(CategoriaTrabajo)
admin.site.register(Material)
admin.site.register(Contacto)
