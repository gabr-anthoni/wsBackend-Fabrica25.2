
from django.urls import path
from .views import home, listar_perfis,ver_perfil , limpar_lista, adicionar_perfil, retirar_perfil, alterar_perfil

urlpatterns = [
    path('', home, name='home'),
    path('lista-perfis/', listar_perfis, name='lista-perfis'), 
    path('adicionar-perfil/', adicionar_perfil, name='adicionar-perfil'),
    path('lista-perfis/perfil/<int:pk>', ver_perfil, name='ver-perfil'),
    path('lista-perfis/perfil/retirar-perfil/<int:pk>', retirar_perfil, name='retirar-perfil'),
    path('lista-perfis/perfil/alterar-perfil/<int:pk>', alterar_perfil, name='alterar-perfil' ),
    path('limpar-lista/',limpar_lista, name='limpar-lista'),
]
