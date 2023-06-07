
from django.urls import path
from .views import index, auth_login, auth_register, busqueda
from .views import crearTrabajo, revisionTrabajo, solicitud, trabajo, cantidadTrabajos, estadoPublicacion

urlpatterns = [
    path('', index,name='index'),
    path('index', index, name='index'),
    path('auth_login', auth_login,name='auth_login'),
    path('registro', auth_register,name='auth_register'),
    path('busqueda', busqueda,name='busqueda'),
    path('crearTrabajo', crearTrabajo,name='crearTrabajo'),
    path('revisionTrabajo', revisionTrabajo,name='revisionTrabajo'),
    path('solicitud', solicitud,name='solicitud'),
    path('trabajo', trabajo,name='trabajo'),
    path('cantidadTrabajos', cantidadTrabajos,name='cantidadTrabajos'),
    path('estadoPublicacion', estadoPublicacion,name='estadoPublicacion'),   
]
