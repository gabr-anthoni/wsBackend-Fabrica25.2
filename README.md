
# Desafio Fábrica de Software 2025.2 Workshop com Django

Este projeto é uma lista de perfis de usuários do GitHub, onde você pode:
- Adicionar perfis
- Editar informações
- Remover usuários da lista
- Visualizar os detalhes de cada perfil<br>
A aplicação utiliza a API pública do GitHub para buscar informações em tempo real sobre os usuários.

🔍 O que cada perfil exibe:
Informações gerais dividade em entidades :

**Perfis do GitHub :**
- Nome do usuário (se estiver disponível)
- Login único (username)

**informações do GitHub :**
- Imagem do perfil
- Link para o perfil no GitHub
- Bio (descrição) do usuário

> [!NOTE]
> Para adicionar ou editar um perfil, você deve usar o login do GitHub do usuário.
> Exemplo:
> Meu nome é: Gabriel Anthoni
> Mas meu login é: gba-anthoni

> [!NOTE]
> Se houver mais de um perfil na lista, será exibido um botão para limpar a lista inteira, removendo todos os perfis de uma vez.

### 🖥️ Áreas do Projeto

Página principal: `http://127.0.0.1:8000/GitList/`

Área administrativa: `http://127.0.0.1:8000/admin/`

### 🔐 Superuser (admin do Django)

Usuário: `admin`

Senha: `123`