
from django.urls import path
from .views import home, listar_perfis, adicionar_perfil, retirar_perfil

urlpatterns = [
    path('', home, name='home'),
    path('lista-perfis', listar_perfis, name='lista-perfis'), 
    path('adicionar-perfil', adicionar_perfil, name='adicionar-perfil'),
    path('retirar-perfil/<int:pk>', retirar_perfil, name='retirar-perfil'),
]
