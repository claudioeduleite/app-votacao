# 5. views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroForm
from .models import QRToken, Voto, Auditoria
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
import qrcode
import io

# Cadastro
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            QRToken.objects.create(usuario=usuario)
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

# Tela de votação
@login_required
def votar(request):
    token = QRToken.objects.get(usuario=request.user)
    if token.usado:
        return HttpResponseForbidden("Você já votou.")

    if request.method == 'POST':
        escolha = request.POST['escolha']
        Voto.objects.create(usuario=request.user, escolha=escolha)
        token.usado = True
        token.save()
        Auditoria.objects.create(usuario=request.user, acao=f"Votou em {escolha}", ip=request.META.get('REMOTE_ADDR'))
        return render(request, 'obrigado.html')

    return render(request, 'votar.html')

# Exibir QR Code
@login_required
def mostrar_qrcode(request):
    token = QRToken.objects.get(usuario=request.user)
    img = qrcode.make(str(token.token))
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return HttpResponse(buf.getvalue(), content_type='image/png')