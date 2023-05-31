
from django.urls import path
from .views import index, login

urlpatterns = [
    path('', index,name='index'),
    path('login', login,name='login'),
    path('registro', index,name='registro'),
    path('busqueda', login,name='busqueda'),
    path('crearTrabajo', index,name='crearTrabajo'),
    path('revisionTrabajo', login,name='revisionTrabajo'),
    path('solicitud', index,name='solicitud'),
    path('trabajo', login,name='trabajo'),
    path('cantidadTrabajos', login,name='cantidadTrabajos'),
    path('estadoPublicacion', index,name='estadoPublicacion'),   
]
