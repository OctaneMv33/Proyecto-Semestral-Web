from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    nombre = forms.CharField(max_length=150)
    snombre = forms.CharField(max_length=150)
    appaterno = forms.CharField(max_length=150)
    apmaterno = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')