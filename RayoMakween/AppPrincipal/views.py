from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Contacto, CategoriaTrabajo,EstadoPublicacion,Publicacion, Material, PublicacionMaterial
from .forms import RegistrationForm, ContactoForm, PublicacionForm
import os 
from django.conf import settings
from datetime import date
from django.shortcuts import render, get_object_or_404
from .templatetags.custom_filters import register

# Create your views here.
#Index
def index(request):
    publicaciones = Publicacion.objects.order_by('-id_publicacion')[:2]
    if request.method =='POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            descripcion = form.cleaned_data['descripcion']
            Contacto.objects.create(correo=correo, telefono=telefono, descripcion=descripcion)
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'index.html', {'publicaciones': publicaciones})
#Login de Usuario
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
#Registro de Usuario
def auth_register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            dvrut = form.cleaned_data['dvrut']
            nombre = form.cleaned_data['nombre']
            snombre = form.cleaned_data['snombre']
            appaterno = form.cleaned_data['appaterno']
            apmaterno = form.cleaned_data['apmaterno']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=email,
            first_name=nombre, second_name=snombre, last_name=appaterno,
            second_last_name=apmaterno, email=email, phone=phone, password=password, run=rut, dv_run = dvrut)
#   En caso de querer logear instantaneamente al usuario. 
#   Se puede utilizar el siguiente codigo, borrando la linea de arriba y usando las dos de abajo. 
#   Almacena el formulario que hiciste en un objeto y lo pasa con la funcion login para ingresarte automaticamente
            #user = User.objects.create_user(username=username, email=email, password=password)
            #login(request, user)
            return redirect('auth_login')
    else:
        form = RegistrationForm()
    return(render(request,'registro.html'))

#Vista Admin
#Revision para aprovar o rechazar
def revisionTrabajo(request, id_publicacion):
    estados_publicacion = EstadoPublicacion.objects.all()
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    cantidad_fotos = sum(
        bool(getattr(publicacion, f"foto{i}")) for i in range(1, 7)
    )
    foto_indices = range(1, cantidad_fotos + 1)
    context = {
        'publicacion': publicacion,
        'foto_indices': foto_indices,
        'estados_publicacion' : estados_publicacion
    }
    return (render(request,'revision_trabajo.html', context))

@login_required
def exit(request):
    logout(request)
    return redirect('auth_login')

# Vistas Cliente
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def solicitud(request):
    return (render(request,'solicitud.html'))

@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def trabajo(request):
    
    return (render(request,'trabajo.html'))

# Vistas Mecánico
# Crear Trabajo
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='index')
def crearTrabajo(request):
    data = CategoriaTrabajo.objects.all()
    categorias = []
    for index, item in enumerate(data):
        id_categtrabajo = 1000 + index * 10
        categorias.append({
            'id_categtrabajo': id_categtrabajo,
            'nombre_categtrabajo': item.nombre_categtrabajo
        })
    objMaterial = Material.objects.all
    context = {
        'data': categorias,
        'material':objMaterial
    }
    if request.method == 'POST':
        user_id = request.user.id
        id_user= User.objects.get(id=user_id)
        form = PublicacionForm(request.POST,request.FILES)
        if form.is_valid():
            materials= request.POST["listaMats"]
            titulo_publicacion = request.POST['titulo_publicacion']
            descripcion_publicacion = request.POST['descripcion_publicacion']
            diagnostico_publicacion = request.POST['diagnostico_publicacion']
            id_categoria = request.POST['id_categoria']
            print(id_categoria)
            materials = materials.split(sep=',')
            materials.pop()
            imagenes = request.FILES['imagenes']
            # Guardar la foto en la carpeta media
            photo_path = os.path.join(settings.MEDIA_ROOT, imagenes.name)
            with open(photo_path, 'wb') as file:
                for chunk in imagenes.chunks():
                    file.write(chunk)        
            fecha_hoy = date.today()
            objCategory = CategoriaTrabajo.objects.get(id_categtrabajo=id_categoria)
            objState = EstadoPublicacion.objects.get(id_estpub=10) 
            #OBJSTATE es uno por que el primer ingreso es de rechazado/en revision
            objPublic = Publicacion.objects.create(
                titulo_publicacion=titulo_publicacion,
                descripcion_publicacion=descripcion_publicacion,
                diagnostico_publicacion=diagnostico_publicacion,
                id_categoria=objCategory,
                fecha_publicacion=fecha_hoy,
                id_user=id_user,
                id_estpub=objState
            )
            objPublic.save()
            for i in materials:
                objMater = Material.objects.get(id_material = i)
                objPublicMat = PublicacionMaterial.objects.create(
                    id_publicacion = objPublic,
                    id_material = objMater
                )
                objPublicMat.save()
            for i, imagen in enumerate(request.FILES.getlist('imagenes')):
                setattr(objPublic, f'foto{i+1}', imagen)
            
            # Guarda la instancia de Publicacion nuevamente para guardar las imágenes
            objPublic.save()
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'crear_trabajo.html', context)
@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
def cantidadTrabajos(request):
    return (render(request,'ver_cantidad_trabajos.html'))

@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
def estadoPublicacion(request):
    return (render(request,'ver_estado_publicacion.html'))

#Listado de busqueda
def lista_trabajos(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_trabajos.html', {'publicaciones': publicaciones})
# Revision aprobada
def detalle_publicacion(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    cantidad_fotos = sum(
        bool(getattr(publicacion, f"foto{i}")) for i in range(1, 7)
    )
    foto_indices = range(1, cantidad_fotos + 1)
    context = {
        'publicacion': publicacion,
        'foto_indices': foto_indices,
    }
    return render(request, 'detalle_trabajo.html', context)

@register.filter
def startswith(value, arg):
    return value.startswith(arg)