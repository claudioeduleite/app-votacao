# 1. models.py (no app "votacao")
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Usuario(AbstractUser):
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

class QRToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    usado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

class Voto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    escolha = models.CharField(max_length=100)
    data_hora = models.DateTimeField(auto_now_add=True)

class Auditoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    acao = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    data_hora = models.DateTimeField(auto_now_add=True)