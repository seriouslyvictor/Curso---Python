"""
SESSION 3 — Template Inheritance + Static Files
Flask Course | SENAI | Desenvolvimento Web com Python
================================================================

OBJETIVO DA SESSAO:
  Parar de copiar e colar navbars — e finalmente ter CSS de verdade.

CONCEITOS NOVOS NESTA SESSAO:
  1. base.html       — o template pai (o "esqueleto" que toda pagina compartilha)
  2. {% block %}     — "buracos" no pai que os filhos preenchem com conteudo proprio
  3. {% extends %}   — diz ao filho qual pai usar
  4. /static         — pasta do Flask para CSS, imagens e JavaScript
  5. url_for('static', filename='...')
                     — a forma CERTA do Flask referenciar arquivos estaticos

COMO RODAR:
  No terminal, dentro desta pasta (session_03/):
    flask --app app.py run --debug

  Depois abra: http://127.0.0.1:5000

NOTA PARA O PROFESSOR:
  Este arquivo implementa o projeto "Site Portfolio Multipaginas" (Free Practice).
  A estrutura de pastas intencional e:
    session_03/
    ├── app.py               <- voce esta aqui
    ├── templates/           <- HTML files (Flask busca aqui automaticamente)
    │   ├── base.html        <- template pai (o esqueleto)
    │   ├── home.html        <- pagina inicial (filho)
    │   ├── about.html       <- sobre mim (filho)
    │   ├── projects.html    <- projetos, com loop (filho)
    │   ├── contact.html     <- contato (filho)
    │   └── credits.html     <- mini-desafio: pagina simples que extende base
    └── static/              <- CSS, imagens, JS (browser busca diretamente)
        ├── css/
        │   └── style.css
        └── images/
            └── (coloque imagens aqui)
"""

from flask import Flask, render_template

# ============================================================
# CRIACAO DO APP
# ============================================================

app = Flask(__name__)
# Flask(__name__) diz ao Flask onde procurar:
#   - a pasta templates/  (para arquivos HTML)
#   - a pasta static/     (para CSS, imagens, JavaScript)
# Se você omitir isso, o Flask não encontra os arquivos!


# ============================================================
# DADOS
# ============================================================
# Em uma aplicacao real, esses dados viriam de um banco de dados.
# Por enquanto, usamos listas e dicionarios Python.
# (Banco de dados vem na Sessao 6 — SQLAlchemy!)

projects = [
    {
        "id": 1,
        "name": "Mini Wikipedia",
        "description": "Meu primeiro app Flask. Seis paginas sobre meus topicos favoritos, cada uma com sua propia rota.",
        "tools": ["Flask", "Python"],
        "is_favorite": True,
    },
    {
        "id": 2,
        "name": "Top 5 Fan Page",
        "description": "Fan site para minhas 5 series favoritas, com templates Jinja2 e paginas de detalhe dinamicas.",
        "tools": ["Flask", "Jinja2", "HTML"],
        "is_favorite": False,
    },
    {
        "id": 3,
        "name": "Portfolio Site",
        "description": "Este site! Construido com heranca de template para que todas as paginas compartilhem o mesmo nav e rodape.",
        "tools": ["Flask", "Jinja2", "CSS", "base.html"],
        "is_favorite": True,
    },
]

# ============================================================
# ROTAS
# ============================================================
# Cada rota e uma funcao Python que devolve uma pagina HTML.
# render_template() substitui o antigo "return string" —
# agora devolvemos arquivos HTML reais da pasta templates/.

@app.route("/")
def home():
    """
    Pagina inicial — ponto de entrada do portfolio.

    Passamos 'current_page' para o template poder destacar
    o link ativo na barra de navegacao (stretch goal da sessao!).
    """
    return render_template("home.html", current_page="home")


@app.route("/sobre")
def about():
    """Pagina Sobre — bio curta do estudante."""
    return render_template("about.html", current_page="about")


@app.route("/projetos")
def projects_page():
    """
    Pagina de Projetos — percorre a lista de projetos.

    Passamos a lista `projects` para o template.
    No template, Jinja2 usara {% for %} para exibir cada projeto.
    (Conceito revisado da Sessao 2, agora com heranca!)
    """
    return render_template("projects.html", projects=projects, current_page="projects")


@app.route("/contato")
def contact():
    """
    Pagina de Contato — so exibe informacoes por enquanto.

    NOTA: Formulario com POST vem na Sessao 5.
    Esta pagina intencionalmente nao tem form —
    o objetivo aqui e mostrar heranca de template, nao capturar dados.
    """
    return render_template("contact.html", current_page="contact")


@app.route("/creditos")
def credits():
    """
    Mini-desafio — resultado do desafio de 3 minutos do bloco de demo:
      "Adicione uma pagina /creditos que extende base.html
       e so tem um titulo dentro do bloco de conteudo."

    NOTA PARA O PROFESSOR:
    Este e o exemplo mais simples de heranca — quase vazio.
    Perfeito para mostrar como o nav e rodape aparecem de graca,
    sem copiar nada. O aluno so escreve o que e unico nesta pagina.
    """
    return render_template("credits.html", current_page="credits")


# ============================================================
# INICIALIZACAO
# ============================================================

if __name__ == "__main__":
    # debug=True habilita:
    #   - Auto-reload quando voce salva um arquivo (sem reiniciar o servidor)
    #   - Mensagens de erro detalhadas no browser
    # NUNCA use debug=True em producao (expoe o codigo-fonte)!
    app.run(debug=True)
