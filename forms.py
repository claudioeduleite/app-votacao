# 4. forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'matricula', 'email', 'password1', 'password2']