from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Contacto, CategoriaTrabajo,EstadoPublicacion,Publicacion, Material, PublicacionMaterial, Solicitud
from .forms import RegistrationForm, ContactoForm, PublicacionForm, SolicitudForm
import os 
from django.conf import settings
from datetime import date
from django.shortcuts import render, get_object_or_404
from .templatetags.custom_filters import register
from django.db.models import Q, Value
from django.views.generic import ListView
from django.db import connection
from django.db.models.functions import Concat
from django.views.defaults import page_not_found

# Create your views here.
#Index
def index(request):
    publicaciones = Publicacion.objects.filter(id_estpub=30).order_by('-id_publicacion')[:5]
    categorias = CategoriaTrabajo.objects.all()
    usuarios = User.objects.all()
    context = {
        'categorias': categorias,
        'usuarios': usuarios,
        'publicaciones': publicaciones
    }
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
    return render(request, 'index.html', context)

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
            user = User.objects.create_user(username=email,
            first_name=nombre, second_name=snombre, last_name=appaterno,
            second_last_name=apmaterno, email=email, phone=phone, password=password, run=rut, dv_run = dvrut)
            group = Group.objects.get(name='Cliente')
            user.groups.set([group])
#   En caso de querer logear instantaneamente al usuario. 
#   Se puede utilizar el siguiente codigo, borrando la linea de arriba y usando las dos de abajo. 
#   Almacena el formulario que hiciste en un objeto y lo pasa con la funcion login para ingresarte automaticamente
            return redirect('registroExitoso')
    else:
        form = RegistrationForm()
    return(render(request,'registro.html'))

#Buscar por categoría pertenece a cliente
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='index')
def buscarPorCategoria(request):
    categorias = CategoriaTrabajo.objects.all()
    context = {
        'categorias' : categorias
    }
    return (render(request, 'buscar_por_categoria.html', context))

#Buscar por mecánico pertenece a cliente
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='index')
def buscarPorMecanico(request): 
    grupoMec = Group.objects.get(name='Mecanico')
    mecanicos = User.objects.filter(groups = grupoMec)
    context = {
        'mecanicos' : mecanicos
    }
    return (render(request, 'buscar_por_mecanico.html', context))

#Registro de Mecánico
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists(), login_url='index')
def registro_mecanico(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
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
            user = User.objects.create_user(username=email,
            first_name=nombre, second_name=snombre, last_name=appaterno,
            second_last_name=apmaterno, email=email, phone=phone, password=password, run=rut, dv_run = dvrut)
            group = Group.objects.get(name='Mecanico')
            user.groups.set([group]) 
            return redirect('registroExitoso')
    else:
        form = RegistrationForm()
    return(render(request,'registro_mecanico.html'))

#Vista Admin
#Revision para aprobar o rechazar
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists(), login_url='index')
def revisionTrabajo(request, id_publicacion):
    estados_publicacion = EstadoPublicacion.objects.filter(Q(id_estpub=20) | Q(id_estpub=30))
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    cantidad_fotos = sum(
        bool(getattr(publicacion, f"foto{i}")) for i in range(1, 7)
    )
    materiales = PublicacionMaterial.objects.filter(id_publicacion=publicacion).values_list('id_material__nombre_material', flat=True)
    foto_indices = range(1, cantidad_fotos + 1)
    context = {
        'publicacion': publicacion,
        'foto_indices': foto_indices,
        'estados_publicacion' : estados_publicacion,
        'materiales' : materiales
    }
    if request.method=='POST':
        estado_revision_id = request.POST.get('estado_revision')
        estado_revision = EstadoPublicacion.objects.get(id_estpub=estado_revision_id)
        fecha_revision = request.POST.get('fechaRevision')
        publicacion.id_estpub = estado_revision
        publicacion.fecha_revision = fecha_revision
        #En caso de rechazo
        if estado_revision_id == '20':
            motivo_modificado = request.POST.get('motivo_rechazo')
            publicacion.motivo_rechazo = motivo_modificado
            publicacion.cant_rechaz += 1
            publicacion.fecha_revision = fecha_revision
        publicacion.save()
        return redirect('listadoTrabajosRevision')
    return (render(request,'revision_trabajo.html', context))

#Admin
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists(), login_url='index')
def dashboardAdmin(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                CONCAT(u.run,'-',u.dv_run) AS RUT,
                CONCAT(u.first_name,' ',u.last_name) AS NOMBRE,
                SUM(CASE WHEN NULLIF(NULLIF(p.id_estpub, 10),20) IS NULL THEN 0 
                WHEN NULLIF(NULLIF(p.id_estpub, 10),20) = 30 THEN 1 END) AS CANTIDAD_ACEPTADOS,
                SUM(CASE WHEN NULLIF(NULLIF(p.id_estpub, 10),30) IS NULL THEN 0 
                WHEN NULLIF(NULLIF(p.id_estpub, 10),30) = 20 THEN 1 END) AS CANTIDAD_RECHAZADOS,
                SUM(CASE WHEN NULLIF(NULLIF(p.id_estpub, 20),30) IS NULL THEN 0 
                WHEN NULLIF(NULLIF(p.id_estpub, 20),30) = 10 THEN 1 END) AS CANTIDAD_PENDIENTES
            FROM 
                appprincipal_user u
                INNER JOIN appprincipal_publicacion p
                ON(u.id = p.id_user)
            GROUP BY
                RUT, NOMBRE
        """)
        datos= cursor.fetchall()
        keys = ['RUT', 'NOMBRE', 'CANTIDAD_ACEPTADOS', 'CANTIDAD_RECHAZADOS', 'CANTIDAD_PENDIENTES']
        datos_dict = [dict(zip(keys, row)) for row in datos]

        context = {
            'datos':datos_dict
        }
    return render(request, 'dashboard_admin.html', context)

# Mecánico
@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
def editarTrabajo(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    cantidad_fotos = sum(
        bool(getattr(publicacion, f"foto{i}")) for i in range(1, 7)
    )
    materiales = PublicacionMaterial.objects.filter(id_publicacion=publicacion)
    foto_indices = range(1, cantidad_fotos + 1)
    data = CategoriaTrabajo.objects.all()
    categorias = []
    for index, item in enumerate(data):
        id_categtrabajo = 1000 + index * 10
        categorias.append({
            'id_categtrabajo': id_categtrabajo,
            'nombre_categtrabajo': item.nombre_categtrabajo
        })
    objMaterial = Material.objects.exclude(nombre_material__in=materiales.values_list('id_material__nombre_material', flat=True))
    context = {
        'data': categorias,
        'publicacion': publicacion,
        'foto_indices': foto_indices,
        'materiales' : materiales,
        'material':objMaterial
    }
    if request.method == 'POST':
        materials= request.POST["listaMats"]
        if 'imagenes' in request.FILES:
            for i in range(1, 7):
                setattr(publicacion, f'foto{i}', None)
            for i, imagen in enumerate(request.FILES.getlist('imagenes')):
                setattr(publicacion, f'foto{i+1}', imagen)
        PublicacionMaterial.objects.filter(id_publicacion=publicacion).delete()
        publicacion.titulo_publicacion = request.POST['titulo_publicacion']
        publicacion.diagnostico_publicacion = request.POST['diagnostico']
        publicacion.descripcion_publicacion = request.POST['descripcion']
        id_categoria = request.POST['id_categoria']
        publicacion.id_categoria = get_object_or_404(CategoriaTrabajo, id_categtrabajo=id_categoria)
        publicacion.id_estpub = EstadoPublicacion.objects.get(id_estpub=10) 
        materials = materials.split(sep=',')
        for i in materials:
                objMater = Material.objects.get(id_material = i)
                objPublicMat = PublicacionMaterial.objects.create(
                    id_publicacion = publicacion,
                    id_material = objMater
                )
                objPublicMat.save()
        publicacion.save()
        return redirect('listaTrabajosRechazados')
    return(render(request, 'editar_trabajo.html',context))

# Mecánico
@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
def listaTrabajosRechazados(request):
    usuarioActual = request.user
    publicaciones = Publicacion.objects.filter(Q(id_estpub=20) & Q(id_user = usuarioActual))
    return(render(request, 'lista_trabajos_rechazados.html', {'publicaciones' : publicaciones}))

@login_required
def exit(request):
    logout(request)
    return redirect('auth_login')

# Vistas Cliente
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def solicitud(request):
    if request.method == 'POST':
        user_id = request.user.id
        id_user= User.objects.get(id=user_id)
        form = SolicitudForm(request.POST)
        if form.is_valid():
            fechaSolicitud = form.cleaned_data['fechaSolicitud']
            descripcionSolicitud = form.cleaned_data['descripcionSolicitud']
            objSolic = Solicitud.objects.create(
                fecha_solicitud = fechaSolicitud,
                descripcion_solicitud = descripcionSolicitud,
                id_user = id_user
            )
            objSolic.save()
            return redirect('index')
        else:
            print(form.errors)

    return (render(request,'solicitud.html'))

@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def trabajo(request):
    return (render(request,'trabajo.html'))

# Vistas Mecánico
# Crear Trabajo
@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
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
                cant_rechaz=0,
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
            return redirect('registroExitoso')
        else:
            print(form.errors)
    return render(request, 'crear_trabajo.html', context)

@user_passes_test(lambda u: u.groups.filter(name='Mecanico').exists(), login_url='index')
def estadoPublicacion(request):
    usuarioActual = request.user
    publicaciones = Publicacion.objects.filter(id_user = usuarioActual)
    context = {
        'publicaciones' : publicaciones
    }
    return (render(request,'ver_estado_publicacion.html', context))

@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists(), login_url='index')
def listadoTrabajosRevision(request):
    publicaciones = Publicacion.objects.filter(id_estpub=10)
    return (render(request, 'lista_trabajos_pendientes.html', {'publicaciones':publicaciones}))


#Listado de busqueda
def lista_trabajos(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_trabajos.html', {'publicaciones': publicaciones})

# Busqueda de categoria
@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def resultados_por_categoria(request):
    categorias = CategoriaTrabajo.objects.all()
    context = {
        'categorias': categorias,
        **SearchResultsViewCategory.as_view()(request).context_data,
    }
    return render(request, 'resultados_por_categoria.html', context)

@user_passes_test(lambda u: u.groups.filter(name='Cliente').exists(), login_url='auth_login')
def resultados_por_mecanico(request):
    grupoMec = Group.objects.get(name='Mecanico')
    mecanicos = User.objects.filter(groups = grupoMec)
    context = {
        'mecanicos' : mecanicos
        **SearchResultsViewMechanics.as_view()(request).context_data,
    }
    return render(request, 'resultados_por_mecanico.html', context)

# Revision aprobada
def detalle_publicacion(request, id_publicacion):
    publicacion = get_object_or_404(Publicacion, id_publicacion=id_publicacion)
    cantidad_fotos = sum(
        bool(getattr(publicacion, f"foto{i}")) for i in range(1, 7)
    )
    foto_indices = range(1, cantidad_fotos + 1)
    materiales = PublicacionMaterial.objects.filter(id_publicacion=publicacion).values_list('id_material__nombre_material', flat=True)
    context = {
        'publicacion': publicacion,
        'foto_indices': foto_indices,
        'materiales': materiales,
    }
    return render(request, 'detalle_trabajo.html', context)

def registroExitoso(request):
    return render(request, 'registro_exitoso.html')

@register.filter
def startswith(value, arg):
    return value.startswith(arg)


class SearchResultsView(ListView):
    model = Publicacion
    template_name = 'lista_trabajos.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            queryset = Publicacion.objects.annotate(
                full_name=Concat('id_user__first_name', Value(' '), 'id_user__last_name')
            ).filter(
                Q(titulo_publicacion__icontains=query) |
                Q(diagnostico_publicacion__icontains=query) |
                Q(descripcion_publicacion__icontains=query) |
                Q(id_categoria__nombre_categtrabajo__icontains=query) |
                Q(full_name__icontains=query)
            ).distinct()
            return queryset
        else:
            return Publicacion.objects.none()

class SearchResultsViewCategory(ListView):
    model = Publicacion
    template_name = 'resultados_por_categoria.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('resultados_por_categoria')
        if query:
            queryset = Publicacion.objects.filter(
                Q(id_categoria__nombre_categtrabajo__icontains=query)
            )          
            return queryset
        else:
            return Publicacion.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorias = CategoriaTrabajo.objects.all()
        context['categorias'] = categorias
        return context
    
class SearchResultsViewMechanics(ListView):
    model = Publicacion
    template_name = 'resultados_por_mecanico.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('resultados_por_mecanico')
        if query:
            queryset = Publicacion.objects.annotate(
                full_name=Concat('id_user__first_name', Value(' '), 'id_user__last_name')
            ).filter(
                Q(full_name__icontains=query)
            ).distinct()
            return queryset
        else:
            return Publicacion.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupoMec = Group.objects.get(name='Mecanico')
        mecanicos = User.objects.filter(groups = grupoMec)
        context['mecanicos'] = mecanicos
        return context

# Organizar código

#Vistas No Registrado

#Vistas Cliente

#Vistas Mecánico

#Vistas Admin

#Clases para búsqueda

#No se encuentra 

def pagina_no_encontrada(request, exception):
    return page_not_found(request, exception, template_name='not_found.html')

def login_view(request):
    if request.method == 'POST':
        if User:
            error_message = 'Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')
