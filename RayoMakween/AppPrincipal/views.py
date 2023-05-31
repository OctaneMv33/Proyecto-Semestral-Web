from django.shortcuts import render

# Create your views here.
def index(request):
    return (render(request,'index.html'))
def login(request):
    return (render(request,'login.html'))
def registro(request):
    return (render(request,'registro.html'))
def busqueda(request):
    return (render(request,'busqueda.html'))
def crearTrabajo(request):
    return (render(request,'crear_trabajo.html'))
def revisionTrabajo(request):
    return (render(request,'revision_trabajo.html'))
def solicitud(request):
    return (render(request,'solicitud.html'))
def trabajo(request):
    return (render(request,'trabajo.html'))
def cantidadTrabajos(request):
    return (render(request,'ver_cantidad_trabajos.html'))
def estadoPublicacion(request):
    return (render(request,'ver_estado_publicacion.html'))