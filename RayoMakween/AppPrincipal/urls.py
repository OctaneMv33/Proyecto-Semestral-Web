
from django.urls import path
from .views import index, auth_login, auth_register, SearchResultsView
from .views import crearTrabajo, revisionTrabajo, solicitud, cantidadTrabajos, estadoPublicacion,exit,lista_trabajos, detalle_publicacion, listadoTrabajosRevision

urlpatterns = [
    path('', index,name='index'),
    path('index', index, name='index'),
    path('auth_login', auth_login,name='auth_login'),
    path('registro', auth_register,name='auth_register'),
    path('crearTrabajo', crearTrabajo,name='crearTrabajo'),
    path('revisionTrabajo/<int:id_publicacion>', revisionTrabajo,name='revisionTrabajo'),
    path('solicitud', solicitud,name='solicitud'),
    path('lista_trabajos', lista_trabajos, name='lista_trabajos'),
    path('trabajo/<int:id_publicacion>', detalle_publicacion, name='detalle_publicacion'),
    path('cantidadTrabajos', cantidadTrabajos,name='cantidadTrabajos'),
    path('estadoPublicacion', estadoPublicacion,name='estadoPublicacion'), 
    path('buscar', SearchResultsView.as_view(), name='search_results'),
    path('listadoTrabajosRevision', listadoTrabajosRevision, name='listadoTrabajosRevision'),
    path('logout',exit,name='exit'),
]
