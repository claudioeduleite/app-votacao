# 6. urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('votar/', views.votar, name='votar'),
    path('qrcode/', views.mostrar_qrcode, name='qrcode'),
]