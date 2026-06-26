# 🚀 Django Rest Framework API - Sistema de Blog e Comentários

Este projeto é uma API REST robusta e escalável desenvolvida em Python utilizando o **Django** e o **Django Rest Framework (DRF)**. O sistema gerencia uma estrutura completa de publicações divididas por categorias, com suporte a comentários aninhados, paginação customizada, filtros avançados e segurança baseada em permissões por objeto.

---

## 📌 Funcionalidades Principais

* **Arquitetura Baseada em ViewSets & Routers:** Endpoints totalmente automatizados sem código manual repetitivo.
* **Dados Aninhados (Nested Routers):** Relação hierárquica perfeita para comentários (ex: `api/posts/<post_id>/comentarios`).
* **Segurança e Permissões:** Autenticação via Token. Leitura pública e modificações restritas apenas ao autor do registo (`IsAuthorOrReadOnly`).
* **Validações Customizadas:** Filtro de palavras não permitidas nos títulos dos posts e regras de consistência de tamanho de campos.
* **Filtros, Busca e Ordenação:** Consultas flexíveis por categorias, usernames, termos de pesquisa e ordenação cronológica.
* **Paginação Sob Medida:** Listagem otimizada configurada para controlo de lotes de registos.

---

## 📂 Estrutura de Endpoints da API

Graças ao uso de `DefaultRouter` e `NestedDefaultRouter`, a API disponibiliza os seguintes caminhos limpos (sem a obrigatoriedade da barra `/` no final):

### 📁 Categorias
* `GET /api/categorias` - Lista todas as categorias.
* `POST /api/categorias` - Cria uma nova categoria (Requer autenticação).
* `GET /api/categorias/<id>` - Detalha uma categoria específica.
* `PUT/PATCH /api/categorias/<id>` - Atualiza uma categoria (Requer equipa administrativa).
* `DELETE /api/categorias/<id>` - Remove uma categoria (Requer equipa administrativa).

### 📝 Posts (Publicações)
* `GET /api/posts` - Lista os posts com paginação (Filtros disponíveis: `?categoria__slug=`, `?autor__username=`, `?search=`, `?ordering=`).
* `POST /api/posts` - Cria um novo post. O autor é vinculado automaticamente ao utilizador autenticado.
* `GET /api/posts/<id>` - Detalha um post específico (inclui o nó `categoria_info`).
* `PUT/PATCH /api/posts/<id>` - Atualiza um post (Apenas o autor do post).
* `DELETE /api/posts/<id>` - Remove um post (Apenas o autor do post).

### 💬 Comentários Aninhados
* `GET /api/posts/<post_pk>/comentarios` - Lista apenas os comentários pertencentes àquele post específico.
* `POST /api/posts/<post_pk>/comentarios` - Cria um comentário associado automaticamente ao post da URL e ao utilizador logado.
* `GET /api/posts/<post_pk>/comentarios/<id>` - Detalha um comentário específico.
* `PUT/PATCH /api/posts/<post_pk>/comentarios/<id>` - Atualiza o comentário (Apenas o autor).
* `DELETE /api/posts/<post_pk>/comentarios/<id>` - Remove o comentário (Apenas o autor).

---

## 🛠️ Tecnologias e Dependências Utilizadas

* **Python 3.x**
* **Django 6.x** (ou versão instalada no ambiente)
* **Django Rest Framework** (Core da API e Autenticação por Token)
* **django-filter** (Para os filtros complexos de URL)
* **drf-nested-routers** (Para o mapeamento das rotas de comentários vinculados aos posts)

---

## ⚙️ Configurações Importantes Implementadas

### 🔒 Autenticação e Segurança
As requisições de escrita exigem o envio do Token de Autenticação no cabeçalho HTTP:
```http
Authorization: Token <sua_chave_de_token>
```

A rota para geração de tokens através de credenciais (username e password) está mapeada em:
POST /api/login

📏 Regras de Validação (Serializers)
Validador Reutilizável (no_badword): Impede a submissão de títulos que contenham palavras ofensivas ou banidas da lista configurada.

Validação de Tamanho Mínimo: Títulos não podem conter menos de 10 caracteres nem iniciar com números.

Lógica de Contexto Cruzado: Se um post for associado a uma categoria, o campo content é obrigado a ter pelo menos 10 caracteres.

📄 Parâmetros de Paginação Customizada
Implementado via classe PostPagination:

page_size = 2 (Exibe 2 itens por padrão por página).

page_query_param = 'page_size' (Permite ao cliente expandir o lote via URL, ex: ?page_size=5).

max_page_size = 10 (Teto máximo de segurança por requisição).

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Como Executar o Projeto Localmente

1° -Clona o repositório:
```
git clone <url-do-teu-repositorio>
cd <nome-da-pasta-do-projeto>
```

2° - Cria e ativa o Ambiente Virtual:
```
# No Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# No Windows (Prompt de Comando):
python -m venv venv
venv\Scripts\activate
```

3° - Instala as dependências do sistema:
```
pip install django djangorestframework django-filter drf-nested-routers
```
4° - Executa as Migrações do Banco de Dados:
```
python manage.py makemigrations
python manage.py migrate
```
5° - Inicia o Servidor de Desenvolvimento:
```
python manage.py runserver
A API estará disponível e pronta para consumo em http://127.0.0.1:8000/api.
```

📄 Licença
Este projeto é de uso livre para consulta, aprendizado e desenvolvimento contínuo.
