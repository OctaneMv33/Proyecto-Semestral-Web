from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import RegistrationForm
# Create your views here.
def index(request):
    return (render(request,'index.html'))
def auth_login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message= 'Nombre de usuario o contraseña incorrecto'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return(render(request,'login.html'))
def auth_register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            snombre = form.cleaned_data['snombre']
            appaterno = form.cleaned_data['appaterno']
            apmaterno = form.cleaned_data['apmaterno']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=email,
            first_name=nombre, second_name=snombre, last_name=appaterno,
            second_last_name=apmaterno, email=email, phone=phone, password=password)
#   En caso de querer logear instantaneamente al usuario. 
#   Se puede utilizar el siguiente codigo, borrando la linea de arriba y usando las dos de abajo. 
#   Almacena el formulario que hiciste en un objeto y lo pasa con la funcion login para ingresarte automaticamente
            #user = User.objects.create_user(username=username, email=email, password=password)
            #login(request, user)
            return redirect('auth_login')
    else:
        form = RegistrationForm()
    return(render(request,'registro.html'))
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
@login_required
def estadoPublicacion(request):
    return (render(request,'ver_estado_publicacion.html'))