"""
SESSION 5 - Forms & User Input (POST)
Flask Course | Desenvolvimento Web com Python
============================================================

OBJETIVO DA SESSAO:
  Entender que um formulario com method="POST" envia dados no CORPO
  da requisicao (invisivel na URL) e que Flask le esses dados com
  request.form. Aprender o padrao de duas rotas: uma para receber
  (POST), outra para exibir (GET).

CONCEITOS NOVOS NESTA SESSAO:
  1. method="POST"              - envia dados no corpo, nao na URL
  2. methods=["GET", "POST"]    - uma rota que aceita dois metodos
  3. request.method             - descobre qual metodo chegou agora
  4. request.form.get("chave")  - le dados de um formulario POST
  5. redirect(url_for(...))     - redireciona para outra rota apos POST
  6. Lista no nivel do modulo   - estado em memoria que persiste entre requests
  7. Padrao Post/Redirect/Get   - POST processa, GET exibe

COMO RODAR:
  No terminal, dentro desta pasta (session_05/):
    flask --app app.py run --debug

  Depois abra:
    http://127.0.0.1:5000

NOTA PARA O PROFESSOR:
  Este arquivo implementa o projeto "Dream Team" com duas rotas separadas:

    /adicionar (GET + POST) -> recebe e processa o formulario
    /elenco    (GET)        -> exibe o elenco montado

  O caminho completo do dado nesta sessao e:

    formulario HTML
      -> corpo da requisicao POST (invisivel na URL)
        -> request.form.get("chave")
          -> Python adiciona na lista
            -> redirect()
              -> navegador faz um GET
                -> render_template exibe o elenco

  O erro mais comum desta sessao: declarar a lista elenco DENTRO
  de uma funcao. Isso a reseta a cada request e os jogadores somem.
  Sempre declarar no nivel do modulo, fora de qualquer funcao.
"""

from flask import Flask, render_template, request, redirect, url_for


# ============================================================
# CRIACAO DA APLICACAO
# ============================================================

aplicacao = Flask(__name__)


# ============================================================
# ESTADO EM MEMORIA - LISTA NO NIVEL DO MODULO
# ============================================================
# CONCEITO NOVO: estado em memoria
#
# Esta lista existe FORA de qualquer funcao, no nivel do modulo.
# Isso significa que ela e criada uma vez quando o servidor inicia
# e persiste enquanto ele estiver rodando.
#
# Cada nova requisicao (cada submit, cada clique) usa A MESMA lista.
# Ela acumula jogadores ao longo das chamadas.
#
# Compare:
#
#   CORRETO - fora das funcoes, sobrevive entre requests:
#   elenco = []          <- aqui no modulo (linha abaixo desta)
#
#   ERRADO - dentro de uma funcao, reseta a cada request:
#   def pagina_adicionar():
#       elenco = []      <- aqui dentro, lista sempre voltaria a []
#
# Limitacao desta abordagem:
#   Ao reiniciar o servidor (Ctrl+C e flask run de novo),
#   a lista volta a ser vazia. Na Sessao 6 vamos resolver isso
#   com um banco de dados que guarda os dados em disco.

elenco = []

# Constante que reflete a regra do esporte: 11 jogadores por time.
# Manter como constante (letras maiusculas) facilita alterar o valor
# em um lugar so, sem precisar cacar o numero 11 por todo o arquivo.
LIMITE_JOGADORES = 11

# Lista de posicoes validas usada para popular o <select> no template.
# Mantida aqui para nao espalhar esses valores entre Python e HTML.
posicoes_validas = ["Goleiro", "Zagueiro", "Lateral", "Meio-campo", "Atacante"]


# ============================================================
# ROTA INICIAL - REDIRECIONA PARA O FORMULARIO
# ============================================================

@aplicacao.route("/")
def pagina_inicial():
    # url_for("pagina_adicionar") gera a string "/adicionar" a partir
    # do nome da funcao, sem escrever o caminho na mao.
    # Vantagem: se a URL da rota mudar, url_for se atualiza sozinho.
    return redirect(url_for("pagina_adicionar"))


# ============================================================
# ROTA DO FORMULARIO - RECEBE O POST E PROCESSA
# ============================================================

@aplicacao.route("/adicionar", methods=["GET", "POST"])
def pagina_adicionar():
    """
    CONCEITO NOVO: methods=["GET", "POST"]

    Por padrao, uma rota Flask aceita apenas GET.
    Ao declarar methods=["GET", "POST"], esta rota passa a aceitar
    os dois metodos na mesma URL /adicionar.

    Dois momentos diferentes chegam aqui:

      1. Navegador abre /adicionar normalmente  -> GET  -> mostrar formulario
      2. Usuario clica em "Adicionar ao Elenco" -> POST -> processar dados

    request.method e a string que nos diz qual dos dois chegou agora.
    """

    # ----------------------------------------------------------
    # CONCEITO NOVO: request.method
    # ----------------------------------------------------------
    # request.method e uma string: "GET", "POST", "PUT", "DELETE"...
    # Aqui usamos um if/else para separar os dois comportamentos.
    if request.method == "POST":

        # -------------------------------------------------------
        # CONCEITO NOVO: request.form
        # -------------------------------------------------------
        # Na Sessao 4 liamos dados da URL com request.args.
        # No POST, os dados nao estao na URL - estao no CORPO da requisicao.
        # O Flask os expoe atraves do objeto request.form.
        #
        # Comparacao direta:
        #
        #   GET  -> dados na URL         -> request.args.get("chave")
        #   POST -> dados no corpo (body) -> request.form.get("chave")
        #
        # A sintaxe e identica. O que muda e onde o dado mora.
        # Tentar ler request.args em um POST vai retornar None.
        # Tentar ler request.form em um GET vai retornar None.
        nome_do_jogador   = request.form.get("nome")
        posicao           = request.form.get("posicao")
        url_da_imagem     = request.form.get("url_imagem")
        numero_da_camisa  = request.form.get("numero_camisa")

        # -------------------------------------------------------
        # REGRA DE NEGOCIO: o elenco tem limite de 11 jogadores.
        # O esporte tem uma regra. O codigo tem uma regra que bate.
        # Verificamos antes de adicionar se ainda ha vaga.
        # -------------------------------------------------------
        if len(elenco) < LIMITE_JOGADORES:
            novo_jogador = {
                "nome":          nome_do_jogador,
                "posicao":       posicao,
                "url_imagem":    url_da_imagem,
                "numero_camisa": numero_da_camisa,
            }
            # append() adiciona o dicionario ao final da lista elenco.
            # Como elenco mora no modulo, essa mudanca persiste.
            elenco.append(novo_jogador)

        # -------------------------------------------------------
        # CONCEITO NOVO: redirect apos POST (Padrao PRG)
        # -------------------------------------------------------
        # Depois de processar um POST, NAO renderizamos uma pagina.
        # Enviamos o navegador para uma rota GET com redirect().
        #
        # Por que isso importa?
        #   Se renderizassemos aqui, o usuario apertaria F5 na pagina
        #   resultante e o navegador perguntaria "Reenviar formulario?".
        #   Se confirmasse, o mesmo jogador seria adicionado de novo.
        #
        #   Com redirect, o F5 apenas recarrega a pagina GET de destino.
        #   Nao ha risco de duplicar o envio.
        #
        # Esse padrao tem nome: Post / Redirect / Get (PRG).
        # E um habito profissional que usaremos em todo POST daqui pra frente.
        return redirect(url_for("pagina_elenco"))

    # ----------------------------------------------------------
    # SE CHEGOU AQUI, E UM GET - MOSTRAR O FORMULARIO
    # ----------------------------------------------------------
    # O if acima so executa quando e POST e SEMPRE retorna dentro dele.
    # Qualquer codigo abaixo deste comentario so roda em requests GET.

    # Calculamos informacoes uteis para o template.
    elenco_cheio    = len(elenco) >= LIMITE_JOGADORES
    vagas_restantes = LIMITE_JOGADORES - len(elenco)

    return render_template(
        "adicionar.html",
        posicoes=posicoes_validas,
        elenco_cheio=elenco_cheio,
        vagas_restantes=vagas_restantes,
        total_jogadores=len(elenco),
        limite=LIMITE_JOGADORES,
    )


# ============================================================
# ROTA DO ELENCO - EXIBE A LISTA (GET PURO)
# ============================================================

@aplicacao.route("/elenco")
def pagina_elenco():
    """
    Esta rota SOMENTE exibe. Ela nunca modifica nada.

    Seu unico trabalho e pegar a lista elenco (que mora no modulo)
    e entrega-la ao template para renderizacao.

    Separar "quem recebe dados" de "quem mostra dados" e o
    coracao do padrao de duas rotas desta sessao:

      /adicionar  (POST) -> processa o formulario, redireciona
      /elenco     (GET)  -> somente exibe o estado atual
    """
    return render_template(
        "elenco.html",
        elenco=elenco,
        total_jogadores=len(elenco),
        limite=LIMITE_JOGADORES,
    )


# ============================================================
# INICIALIZACAO
# ============================================================

if __name__ == "__main__":
    # debug=True: recarrega o servidor ao salvar, mostra erros no navegador.
    # Em producao, debug=True deve ficar desligado.
    aplicacao.run(debug=True)
