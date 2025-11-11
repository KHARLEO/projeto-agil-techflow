[README.md](https://github.com/user-attachments/files/23468429/README.md)
# Login CRUD (Flask) - Projeto para entrega

Instruções básicas para rodar localmente.

### Setup
1. criar venv:
   - Windows (PowerShell): `python -m venv .venv` e depois `.venv\Scripts\Activate.ps1`
   - Linux/macOS: `python3 -m venv .venv` e `source .venv/bin/activate`
2. instalar dependências:
   `pip install -r requirements.txt`
3. criar DB:
   `python -c "from app import create_app; from models import db; app = create_app(); with app.app_context(): db.create_all()"`
4. rodar:
   `python -m flask run`

### Notas
- Banco: SQLite (instance/app.db)
- Testes: `pytest -q`
teste

🧱 Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade
🎯 Objetivo do Projeto

Este projeto tem como objetivo aplicar os conceitos de Engenharia de Software e Metodologias Ágeis através da criação de um CRUD de Login em Flask (Python), versionado e controlado no GitHub.
Durante o desenvolvimento, foram utilizadas práticas de controle de versão, integração contínua (CI) e gestão ágil com Kanban.

⚙️ Tecnologias Utilizadas

Linguagem: Python 3.13

Framework Web: Flask

Banco de Dados: SQLite

ORM: SQLAlchemy

Autenticação: Flask-Login

Formulários e Validação: Flask-WTF + Email Validator

Testes: Pytest

CI/CD: GitHub Actions

Gestão Ágil: GitHub Projects (Kanban)

🧩 Estrutura do Projeto
login_crud/
├── app.py
├── models.py
├── forms.py
├── requirements.txt
├── README.md
├── instance/
│   └── app.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── profile.html
│   ├── users.html
│   ├── edit_user.html
│   └── reset_password.html
├── tests/
│   └── test_auth.py
└── .github/
    └── workflows/
        └── ci.yml

🧠 Funcionalidades (CRUD + Login)

✅ Cadastrar usuário (Create)
✅ Listar usuários (Read)
✅ Editar dados de usuário (Update)
✅ Excluir usuário (Delete)
✅ Login e Logout
✅ Proteção de rotas (apenas usuários logados acessam certas páginas)
✅ Recuperação de senha (mudança de escopo simulada)

💾 Como Executar o Projeto Localmente
1️⃣ — Clonar o repositório
git clone https://github.com/seu-usuario/login_crud.git
cd login_crud

2️⃣ — Criar e ativar o ambiente virtual

Windows (PowerShell):

python -m venv .venv
.venv\Scripts\Activate.ps1

3️⃣ — Instalar as dependências
pip install -r requirements.txt

4️⃣ — Criar o banco de dados
python


Dentro do console Python:

from app import create_app
from models import db
app = create_app()
with app.app_context():
    db.create_all()
exit()

5️⃣ — Rodar o servidor
python -m flask run


➡️ Acesse no navegador: http://127.0.0.1:5000

🧪 Executando os Testes Automatizados
pytest -q


O Pytest realiza testes de registro e login, validando o funcionamento do CRUD.

🔁 Integração Contínua (GitHub Actions)

O projeto possui um workflow configurado em .github/workflows/ci.yml que:

Instala as dependências

Executa os testes automaticamente a cada push ou pull request

Isso garante qualidade de código contínua.

📊 Gestão Ágil com Kanban

No GitHub Projects, foi criado um quadro Kanban com as seguintes colunas:

A Fazer: tarefas planejadas (ex: criar modelo User, configurar banco)

Em Progresso: tarefas sendo desenvolvidas

Concluído: tarefas finalizadas

Cards criados:

Estrutura do Projeto

CRUD de Usuário

Sistema de Login

Templates HTML

Testes Automatizados

Pipeline CI

Mudança de Escopo: Reset de Senha

🔄 Mudança de Escopo (Gestão de Mudanças)

Durante o desenvolvimento, foi adicionada uma nova funcionalidade:

🔐 “Recuperar senha do usuário via formulário simples.”

Essa mudança foi implementada com o commit:

feat(scope): adicionar endpoint basico para reset de senha (mudanca de escopo)


E registrada no Kanban como um novo card (“Reset de Senha”).

🧾 Histórico de Commits (resumo)
Nº	Tipo	Mensagem
1	chore	inicializa repositório com README e .gitignore
2	chore	criar estrutura inicial do projeto
3	feat	configurar app Flask e banco de dados
4	feat(models)	adicionar model User
5	feat(forms)	adicionar formulários de login e registro
6	feat(auth)	implementar rotas de login e registro
7	feat(crud)	adicionar rotas de edição e exclusão de usuário
8	feat(templates)	adicionar templates HTML
9	test	adicionar testes com pytest
10	ci	configurar GitHub Actions
11	docs	atualizar README com instruções
12	feat(scope)	adicionar funcionalidade de reset de senha
13	chore	cleanup e comentários finais
👥 Autoria

Aluno: Leonardo Kalil
Disciplina: Engenharia de Software
Tema: Construindo um Projeto Ágil no GitHub
Professor: (coloque o nome do seu professor)
Instituição: (coloque o nome da sua faculdade)
