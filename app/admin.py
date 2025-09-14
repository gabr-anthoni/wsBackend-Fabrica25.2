from django.contrib import admin
from .models import GitHubNome, GitHubInfo

# Mandar o modelo lá pro django admin.
admin.site.register(GitHubNome)
admin.site.register(GitHubInfo)
