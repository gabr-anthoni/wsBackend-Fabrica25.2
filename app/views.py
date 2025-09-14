
from django.shortcuts import render, redirect, get_object_or_404
from .models import GitHubPerfil
import requests

# Home
def home(request):
    return render(request, 'html/home.html')

# Lista de perfis
def listar_perfis(request):
    perfis = GitHubPerfil.objects.all()
    return render(request, 'html/lista.html', {'perfis':perfis})

# Adicionar perfil a lista
def adicionar_perfil(request):
    if request.method == 'POST':
        # Pegar o input da página 'adicionar.html'
        username = request.POST.get('login-perfil')
        # Testa na API do github
        url = f"https://api.github.com/users/{username}"
        # Resposta
        response = requests.get(url)

        if response.status_code == 200:
            # Pegar resposta em json, é tipo biblioteca em python
            data = response.json()

            # Colocar no model pra salvar dps.
            perfil = GitHubPerfil(
                img   = data.get('avatar_url'),
                nome  = data.get('name') or '', # Caso não tenha nada no nome.
                login = data.get('login'),
                site  = data.get('html_url'),
                bio   = data.get('bio') or '',
            )

            # Evitar o mesmo perfil repitido na lista.
            try:
                perfil.save()  # Salva direto no banco de dados
                return redirect('lista-perfis')
            except Exception: # ERRO DE PERFIL JÁ NA LISTA
                erro = f"Perfil '{username}' já está na lista"
                return render(request, 'html/adicionar.html', {'erro': erro})

        else: # ERRO DE PERFIL NÃO ENCONTRADO
            erro = f"Perfil '{username}' não encontrado."
            return render(request, 'html/adicionar.html', {'erro': erro})

    return render(request, 'html/adicionar.html')

# Retirar perfil da lista
def retirar_perfil(request, pk):
    # Pegar pefil pelo ID/PK
    perfil = GitHubPerfil.objects.get(pk=pk)
    if request.method == 'POST':
        # Retirar perfil e voltar para 'lista.html'
        perfil.delete()
        return redirect('lista-perfis')
    return render(request, 'html/retirar.html', {'perfil': perfil})

# Alterar perfil da lista
def alterar_perfil(request, pk):
    perfil = get_object_or_404(GitHubPerfil, pk=pk)
    # Salvar o essencial.
    img_save = perfil.img
    nome_save = perfil.nome or perfil.login

    if request.method == 'POST':
        
        # Pegar o input da página 'alterar.html'
        username = request.POST.get('login-perfil')
        # Testa na API do github
        url = f"https://api.github.com/users/{username}"
        # Resposta
        response = requests.get(url)

        if response.status_code == 200:
            # Pegar resposta em json, é tipo biblioteca em python
            data = response.json()

            # Alterar informações
            perfil.img   = data.get('avatar_url')
            perfil.nome  = data.get('name') or ''
            perfil.login = data.get('login')
            perfil.site  = data.get('html_url')
            perfil.bio   = data.get('bio') or ''
            try:
                perfil.save()
                return redirect('lista-perfis')
            except Exception: # ERRO DE PERFIL JÁ NA LISTA
                erro = f"Perfil '{username}' já está na lista"
                return render(request, 'html/alterar.html', {'erro': erro,'img': img_save,'nome': nome_save})
            
            
        else: # ERRO DE PERFIL NÃO ENCONTRADO
            erro = f"Usuário '{username}' não encontrado."
            return render(request, 'html/alterar.html', {'erro': erro,'img': img_save,'nome': nome_save})

    return render(request, 'html/alterar.html', {'img': img_save,'nome': nome_save})