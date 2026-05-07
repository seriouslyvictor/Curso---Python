"""
SESSION 4 - Forms & User Input (GET)
Flask Course | Desenvolvimento Web com Python
============================================================

OBJETIVO DA SESSAO:
  Entender que um formulario com method="GET" coloca dados na URL
  e que Flask le esses dados com request.args.

CONCEITOS NOVOS NESTA SESSAO:
  1. <form method="GET">      - formulario que envia dados pela URL
  2. name=""                  - nome da chave que aparece na query string
  3. request.args             - dicionario especial com os dados da URL
  4. request.args.get("chave") - forma segura de ler uma chave da URL
  5. Estado vazio             - pagina aberta antes de qualquer envio
  6. try/except float()       - validacao amigavel para entrada numerica

COMO RODAR:
  No terminal, dentro desta pasta (session_04/):
    flask --app app.py run --debug

  Depois abra:
    http://127.0.0.1:5000

NOTA PARA O PROFESSOR:
  Este arquivo implementa o projeto "Conversor Universal".
  Ele usa UMA rota e UM template de proposito. Nesta aula, o foco e
  perceber o caminho completo do dado:

    formulario HTML -> URL do navegador -> request.args -> Python -> template

  A repeticao dos if/elif e intencional. Ela deixa visivel que o HTML
  apenas envia strings; quem decide o significado de cada opcao e o Python.
"""

from flask import Flask, render_template, request


# ============================================================
# CRIACAO DA APLICACAO
# ============================================================

aplicacao = Flask(__name__)


# ============================================================
# DADOS QUE ALIMENTAM O SELECT DO TEMPLATE
# ============================================================
# Cada dicionario representa uma opcao do <select>.
# O campo "valor" e o texto tecnico que vai para a URL.
# O campo "rotulo" e o texto amigavel que o usuario ve na tela.
#
# Exemplo:
#   Se o usuario escolher "Celsius -> Fahrenheit", a URL fica:
#     /?valor=23&tipo=celsius_para_fahrenheit
#
# Repare que "tipo" vem do atributo name="tipo" no HTML.
# O Flask nao inventa esse nome. Ele apenas le o que o formulario enviou.

tipos_de_conversao = [
    {
        "valor": "celsius_para_fahrenheit",
        "rotulo": "Celsius -> Fahrenheit",
    },
    {
        "valor": "fahrenheit_para_celsius",
        "rotulo": "Fahrenheit -> Celsius",
    },
    {
        "valor": "quilogramas_para_libras",
        "rotulo": "Quilogramas -> Libras",
    },
    {
        "valor": "centimetros_para_polegadas",
        "rotulo": "Centimetros -> Polegadas",
    },
    {
        "valor": "quilometros_para_milhas",
        "rotulo": "Quilometros -> Milhas",
    },
    {
        "valor": "reais_para_dolares",
        "rotulo": "Reais (BRL) -> Dolares (USD)",
    },
    {
        "valor": "hectares_para_campos",
        "rotulo": "Hectares -> Campos de futebol",
    },
]


# ============================================================
# ROTA PRINCIPAL
# ============================================================

@aplicacao.route("/")
def pagina_conversor():
    """
    Exibe o formulario e, quando ele for enviado por GET, calcula a conversao.

    IMPORTANTE:
    Esta rota tem dois momentos diferentes:

    1. Primeira visita:
       O usuario ainda nao enviou o formulario.
       A URL esta limpa: /
       Nesse caso, nao existe "valor" em request.args.

    2. Depois do envio:
       O formulario coloca dados na URL.
       Exemplo: /?valor=25&tipo=celsius_para_fahrenheit
       Nesse caso, request.args ja tem os dados para o Python calcular.

    Esse teste de "ja foi enviado ou nao?" e chamado aqui de estado vazio.
    Ele evita tentar converter algo que ainda nao existe.
    """

    # ------------------------------------------------------------
    # ESTADO INICIAL DAS VARIAVEIS
    # ------------------------------------------------------------
    # Comecamos com tudo vazio porque a primeira visita ainda nao tem resultado.
    # Depois, se o formulario tiver sido enviado, essas variaveis serao preenchidas.
    formulario_foi_enviado = "valor" in request.args
    valor_digitado = request.args.get("valor", "")
    tipo_escolhido = request.args.get("tipo", "celsius_para_fahrenheit")

    resultado_formatado = None
    formula_usada = None
    mensagem_de_erro = None

    # ------------------------------------------------------------
    # LEITURA DOS DADOS DA URL
    # ------------------------------------------------------------
    # request.args funciona como um dicionario somente de leitura.
    # Se a URL for:
    #   /?valor=23&tipo=celsius_para_fahrenheit
    #
    # Entao:
    #   request.args.get("valor") -> "23"
    #   request.args.get("tipo")  -> "celsius_para_fahrenheit"
    #
    # Repare: tudo chega como TEXTO. Mesmo "23" chega como string.
    # Por isso usamos float() antes de fazer contas.
    if formulario_foi_enviado:
        try:
            numero_digitado = float(valor_digitado)

            # ------------------------------------------------------------
            # CONDICIONAIS DE CONVERSAO
            # ------------------------------------------------------------
            # O <select> envia uma string. O Python compara essa string
            # e decide qual formula aplicar. Esta e a ponte entre:
            #   opcao visual no HTML -> regra de negocio em Python
            if tipo_escolhido == "celsius_para_fahrenheit":
                resultado = (numero_digitado * 9 / 5) + 32
                resultado_formatado = f"{numero_digitado:.2f} C = {resultado:.2f} F"
                formula_usada = "Formula: (C x 9/5) + 32"

            elif tipo_escolhido == "fahrenheit_para_celsius":
                resultado = (numero_digitado - 32) * 5 / 9
                resultado_formatado = f"{numero_digitado:.2f} F = {resultado:.2f} C"
                formula_usada = "Formula: (F - 32) x 5/9"

            elif tipo_escolhido == "quilogramas_para_libras":
                resultado = numero_digitado * 2.20462
                resultado_formatado = f"{numero_digitado:.2f} kg = {resultado:.2f} lb"
                formula_usada = "Formula: kg x 2.20462"

            elif tipo_escolhido == "centimetros_para_polegadas":
                resultado = numero_digitado / 2.54
                resultado_formatado = f"{numero_digitado:.2f} cm = {resultado:.2f} pol"
                formula_usada = "Formula: cm / 2.54"

            elif tipo_escolhido == "quilometros_para_milhas":
                resultado = numero_digitado * 0.621371
                resultado_formatado = f"{numero_digitado:.2f} km = {resultado:.2f} mi"
                formula_usada = "Formula: km x 0.621371"

            elif tipo_escolhido == "reais_para_dolares":
                # Taxa fixa para fins didaticos.
                # Em um app real, essa taxa viria de uma API ou banco de dados.
                taxa_fixa_brl_para_usd = 5.00
                resultado = numero_digitado / taxa_fixa_brl_para_usd
                resultado_formatado = f"R$ {numero_digitado:.2f} = US$ {resultado:.2f}"
                formula_usada = "Formula: reais / 5.00 (taxa fixa da aula)"

            elif tipo_escolhido == "hectares_para_campos":
                # Um campo de futebol oficial varia de tamanho.
                # Aqui usamos uma aproximacao comum: 1 campo ~= 0.714 hectare.
                resultado = numero_digitado / 0.714
                resultado_formatado = f"{numero_digitado:.2f} ha = {resultado:.2f} campos"
                formula_usada = "Formula: hectares / 0.714"

            else:
                # Este else protege contra valores inesperados na URL.
                # Um usuario pode editar a URL manualmente, entao nunca confie
                # cegamente nos dados que chegam do navegador.
                mensagem_de_erro = "Tipo de conversao desconhecido. Escolha uma opcao da lista."

        except ValueError:
            # float("banana") gera ValueError.
            # Em vez de deixar o Flask mostrar uma tela de erro tecnica,
            # mostramos uma mensagem que o usuario consegue entender.
            mensagem_de_erro = "Digite um numero valido. Exemplo: 25, 3.5 ou 100."

    # ------------------------------------------------------------
    # ENVIO DOS DADOS PARA O TEMPLATE
    # ------------------------------------------------------------
    # render_template entrega variaveis Python para o HTML.
    # O template decide como mostrar cada variavel usando Jinja2:
    #   {{ variavel }} para exibir
    #   {% if condicao %} para controlar blocos
    return render_template(
        "conversor.html",
        tipos_de_conversao=tipos_de_conversao,
        formulario_foi_enviado=formulario_foi_enviado,
        valor_digitado=valor_digitado,
        tipo_escolhido=tipo_escolhido,
        resultado_formatado=resultado_formatado,
        formula_usada=formula_usada,
        mensagem_de_erro=mensagem_de_erro,
    )


# ============================================================
# INICIALIZACAO
# ============================================================

if __name__ == "__main__":
    # debug=True e otimo para aprender:
    #   - recarrega o servidor quando salvamos o arquivo
    #   - mostra erros detalhados no navegador
    #
    # Em producao, debug=True deve ficar desligado.
    aplicacao.run(debug=True)
