from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User, Contacto, Publicacion, CategoriaTrabajo
from multiupload.fields import MultiFileField


class RegistrationForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    snombre = forms.CharField(max_length=150)
    appaterno = forms.CharField(max_length=150)
    apmaterno = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    rut = forms.IntegerField(max_value=99999999)
    dvrut = forms.CharField(max_length=1)
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
class SolicitudForm(forms.Form):
    fechaSolicitud = forms.DateField()
    descripcionSolicitud = forms.CharField(max_length=500)

class ContactoForm(forms.Form):
    correo = forms.EmailField()
    telefono = forms.IntegerField()
    descripcion = forms.CharField(max_length=500)

class PublicacionForm(forms.Form):
    titulo_publicacion = forms.CharField(max_length=100)
    diagnostico_publicacion = forms.CharField(max_length=500)
    descripcion_publicacion = forms.CharField(max_length=1000)
    imagenes = MultiFileField(min_num=1, max_num=6, max_file_size=1024*1024*5)
    id_categoria = forms.ModelChoiceField(queryset=CategoriaTrabajo.objects.all())

    