from .models import Publicacion
def numero_publicaciones_usuario(request):
    numero_publicaciones = 0
    if request.user.is_authenticated:
        id_usuario = request.user.id
        id_estpub = 20
        numero_publicaciones = Publicacion.objects.filter(id_user=id_usuario, id_estpub=id_estpub).count()

    return {'numero_publicaciones': numero_publicaciones}