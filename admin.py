# 2. admin.py
from django.contrib import admin
from .models import Usuario, QRToken, Voto, Auditoria
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario, UserAdmin)
admin.site.register(QRToken)
admin.site.register(Voto)
admin.site.register(Auditoria)