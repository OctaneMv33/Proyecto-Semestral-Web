from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return (render(request,'index.html'))
def auth_login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message= 'Nombre de usuario o contraseña incorrecto'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return(render(request,'login.html'))
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