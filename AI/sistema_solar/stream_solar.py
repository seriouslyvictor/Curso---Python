import streamlit as st
from google import genai
from google.genai import types

# ── Configuração ──────────────────────────────────────────────────
cliente = genai.Client(api_key=st.secrets["GEMINI_KEY"])
MODEL = "gemini-2.5-flash"

# Este dicionário usa o nome da aba como chave e o nome do planeta como valor.
PLANETAS = {
    "☿ Mercúrio": "Mercúrio",
    "♀ Vênus":    "Vênus",
    "🌍 Terra":   "Terra",
    "🔴 Marte":   "Marte",
    "🟠 Júpiter": "Júpiter",
    "🪐 Saturno": "Saturno",
    "🔵 Urano":   "Urano",
    "🌊 Netuno":  "Netuno",
}


def criar_instrucao(planeta):
    return f"""Você é um especialista apaixonado pelo planeta {planeta}.
Responda APENAS sobre {planeta} e o sistema solar quando relevante.
Seja preciso cientificamente, mas use linguagem acessível para adolescentes.
Se perguntarem sobre outro planeta, diga educadamente que sua especialidade
é {planeta} e que cada planeta tem seu próprio especialista neste app."""


def chave_historico(planeta):
    """Gera uma chave única de session_state para cada planeta."""
    return f"historico_{planeta.lower()}"


def inicializar_historico(planeta):
    """Cria a lista de histórico no session_state se ainda não existir."""
    chave = chave_historico(planeta)
    if chave not in st.session_state:
        st.session_state[chave] = []


def renderizar_chat(planeta):
    """
    Renderiza o histórico e o input de um planeta específico.
    Toda a lógica de chat fica aqui — chamada uma vez por aba.
    """
    inicializar_historico(planeta)
    chave = chave_historico(planeta)

    # ── Exibe o histórico existente ───────────────────────────────
    for mensagem in st.session_state[chave]:
        role_display = "user" if mensagem["role"] == "user" else "assistant"
        with st.chat_message(role_display):
            st.write(mensagem["parts"][0]["text"])

    # ── Input do usuário ──────────────────────────────────────────
    entrada = st.chat_input(
        f"Pergunte sobre {planeta}...",
        key=f"input_{planeta}"    # ← cada aba precisa de uma chave única!
    )

    if entrada:
        # Mostra a mensagem do usuário
        with st.chat_message("user"):
            st.write(entrada)

        # Adiciona ao histórico deste planeta
        st.session_state[chave].append({
            "role": "user",
            "parts": [{"text": entrada}]
        })

        # Chama a API
        with st.chat_message("assistant"):
            with st.spinner(f"Consultando especialista em {planeta}..."):
                config = types.GenerateContentConfig(
                    system_instruction=criar_instrucao(planeta)
                )
                resposta = cliente.models.generate_content(
                    model=MODEL,
                    contents=st.session_state[chave],
                    config=config
                )
                texto = resposta.text

            st.write(texto)

        # Adiciona resposta ao histórico
        st.session_state[chave].append({
            "role": "model",
            "parts": [{"text": texto}]
        })


# ── Interface principal ───────────────────────────────────────────
st.title("🪐 Explorador do Sistema Solar")
st.write("Escolha um planeta e converse com seu especialista dedicado.")

# st.tabs() recebe uma lista de nomes e devolve uma lista de contextos
abas = st.tabs(list(PLANETAS.keys()))

# Mantemos a correspondência pelo índice para deixar o fluxo explícito.
nomes_abas = list(PLANETAS.keys())
for indice in range(len(nomes_abas)):
    planeta = PLANETAS[nomes_abas[indice]]
    with abas[indice]:
        renderizar_chat(planeta)
