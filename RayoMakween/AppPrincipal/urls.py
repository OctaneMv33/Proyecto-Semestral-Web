
from django.urls import path
from .views import index, auth_login, auth_register, SearchResultsView,registro_mecanico, SearchResultsViewCategory, SearchResultsViewMechanics, registroExitoso
from .views import crearTrabajo, revisionTrabajo, solicitud,estadoPublicacion,exit,lista_trabajos, detalle_publicacion, listadoTrabajosRevision,dashboardAdmin, listaTrabajosRechazados, editarTrabajo, buscarPorCategoria, buscarPorMecanico

urlpatterns = [
    path('', index,name='index'),
    path('index', index, name='index'),
    path('auth_login', auth_login,name='auth_login'),
    path('registro_mecanico', registro_mecanico,name='registro_mecanico'),
    path('registro', auth_register,name='auth_register'),
    path('crearTrabajo', crearTrabajo,name='crearTrabajo'),
    path('revisionTrabajo/<int:id_publicacion>', revisionTrabajo,name='revisionTrabajo'),
    path('solicitud', solicitud,name='solicitud'),
    path('lista_trabajos', lista_trabajos, name='lista_trabajos'),
    path('trabajo/<int:id_publicacion>', detalle_publicacion, name='detalle_publicacion'),
    path('estadoPublicacion', estadoPublicacion,name='estadoPublicacion'), 
    path('buscar', SearchResultsView.as_view(), name='search_results'),
    path('listadoTrabajosRevision', listadoTrabajosRevision, name='listadoTrabajosRevision'),
    path('listaTrabajosRechazados',listaTrabajosRechazados,name='listaTrabajosRechazados'),
    path('editarTrabajo/<int:id_publicacion>', editarTrabajo, name='editarTrabajo'),
    path('buscarPorMecanico', buscarPorMecanico, name='buscarPorMecanico'),
    path('buscarPorCategoria', buscarPorCategoria, name='buscarPorCategoria'),
    path('resultados_por_categoria', SearchResultsViewCategory.as_view(), name='resultados_por_categoria'),
    path('resultados_por_mecanico', SearchResultsViewMechanics.as_view(), name='resultados_por_mecanico'),
    path('dashboardAdmin', dashboardAdmin, name='dashboardAdmin'),
    path('logout',exit,name='exit'),
    path('registroExitoso', registroExitoso, name='registroExitoso')
]
