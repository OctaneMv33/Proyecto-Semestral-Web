from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User


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
        

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Cliente')  # Nombre del grupo por defecto
        instance.groups.add(group)