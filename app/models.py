from django.db import models

class GitHubPerfil(models.Model):

    # ( max_leght )    --> Máximo de caracteres
    # ( verbose_name ) --> Nome que aparece no django Admin
    # ( black )        --> Não é obrigatório no formulário
    # ( unique )       --> É unico.

    # nome do perfil   :
    nome  = models.CharField(max_length=255, verbose_name="Nome", blank=True)
    # login do perfil  :
    login = models.CharField(max_length=255, verbose_name="Login (Nome original)", unique=True)
    # Imagem do perfil :
    img   = models.URLField(verbose_name="Avatar URL")
    # URL do perfil    :
    site  = models.URLField(verbose_name="URL do Perfil")
    # Bio do perfil    :
    bio   = models.CharField(max_length=160,verbose_name="Bio",blank=True)

    class Meta:
        # Nomes que vão aparecer no django admin
        verbose_name = "Perfil do GitHub"
        verbose_name_plural = "Lista de perfis GitHub" # (Por algum motivo, só este funciona)

    # Como ele vai aparecer lá no django Admin
    def __str__(self):
        if self.nome:
            return f"{self.nome} | {self.login}" # Se tiver nome
        else:
            return self.login # Se apenas tiver o login
    