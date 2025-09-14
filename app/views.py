
from django.shortcuts import render, redirect, get_object_or_404
from .models import GitHubNome, GitHubInfo
import requests

# Home ==============================================================================
def home(request):
    # Quantidade de perfis salvos na lista
    quantidade_de_perfis = GitHubNome.objects.all().count()
    return render(request, 'html/home.html', {"valor": quantidade_de_perfis})

# Lista de perfis ===================================================================
def listar_perfis(request):
    # Perfis com todas a suas informações
    perfis = GitHubNome.objects.all()
    return render(request, 'html/lista.html', {'perfis':perfis})

# Ver perfil =======================================================================
def ver_perfil(request, pk):
    perfil = GitHubNome.objects.get(pk=pk)
    infos = GitHubInfo.objects.get(pk=pk)
    return render(request, 'html/perfil.html', {'perfil': perfil,'infos': infos})

# Adicionar perfil a lista ==========================================================
def adicionar_perfil(request): 
    if request.method == 'POST':
        username = request.POST.get('login-perfil')
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            try:
                # Primeiro, salva o perfil básico
                perfil = GitHubNome(
                    nome  = data.get('name') or '',
                    login = data.get('login'),
                )
                perfil.save()

                # Depois, salva as estatísticas relacionadas
                estatisticas = GitHubInfo(
                    perfil = perfil,
                    img    = data.get('avatar_url'),
                    site   = data.get('html_url'),
                    bio    = data.get('bio') or '',
                )
                estatisticas.save()

                return redirect('lista-perfis')

            except Exception:
                erro = f"Perfil '{username}' já está na lista"
                return render(request, 'html/adicionar.html', {'erro': erro})

        else:
            erro = f"Usuário '{username}' não encontrado."
            return render(request, 'html/adicionar.html', {'erro': erro})

    return render(request, 'html/adicionar.html')

# Retirar perfil da lista ===========================================================
def retirar_perfil(request, pk):
    # Pegar pefil pelo ID/PK
    perfil = GitHubNome.objects.get(pk=pk)
    infos = GitHubInfo.objects.get(pk=pk)
    if request.method == 'POST':
        # Retirar perfil e voltar para 'lista.html'
        perfil.delete()
        infos.delete()
        return redirect('lista-perfis')
    return render(request, 'html/retirar.html', {'perfil': perfil,'infos': infos})

# Alterar perfil da lista ===========================================================
def alterar_perfil(request, pk):
    perfil = get_object_or_404(GitHubNome, pk=pk)
    infos  = get_object_or_404(GitHubInfo, pk=pk)
    # Salvar o essencial.
    img_save  = infos.img
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
            perfil.nome  = data.get('name') or ''
            perfil.login = data.get('login')
            infos.img    = data.get('avatar_url')
            infos.site   = data.get('html_url')
            infos.bio    = data.get('bio') or ''
            try:
                perfil.save()
                infos.save()
                return redirect('lista-perfis')
            except Exception: # ERRO DE PERFIL JÁ NA LISTA
                erro = f"Perfil '{username}' já está na lista"
                return render(request, 'html/alterar.html', {'erro': erro,'img': img_save,'nome': nome_save})
            
            
        else: # ERRO DE PERFIL NÃO ENCONTRADO
            erro = f"Usuário '{username}' não encontrado."
            return render(request, 'html/alterar.html', {'erro': erro,'img': img_save,'nome': nome_save})

    return render(request, 'html/alterar.html', {'img': img_save,'nome': nome_save})

# limpar lista ======================================================================
def limpar_lista(request):
    # Pegar tudo do primeiro perfil
    primeiro_perfil = GitHubInfo.objects.all().first()
    # Pegar tudo do segundo perfil
    ultimo_perfil = GitHubInfo.objects.all().last()
    if request.method == 'POST':
        GitHubNome.objects.all().delete() # Pega todos os perfis e deleta
        GitHubInfo.objects.all().delete()
        return redirect('lista-perfis')
    return render(request, 'html/cls.html', {"img1": primeiro_perfil.img, "img2": ultimo_perfil.img})
