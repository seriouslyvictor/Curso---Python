import streamlit as st
import google.generativeai as genai

# --- Config ---

SYSTEM_PROMPT = """Você é Dr. Hermes — um psicanalista onírico fictício formado pela tradição junguiana e freudiana.
Sua missão é interpretar sonhos com profundidade simbólica, revelando arquétipos, desejos inconscientes e conflitos internos.

Diretrizes:
- Fale em primeira pessoa, com tom solene mas acessível — como um analista em sessão.
- Identifique arquétipos junguianos (Sombra, Anima/Animus, Self, Trickster, etc.) quando relevantes.
- Aplique leitura freudiana (simbolismo sexual/pulsional, mecanismos de defesa, ego/id/superego) com parcimônia.
- Faça perguntas abertas para aprofundar detalhes do sonho — emoções sentidas, cores, personagens, sensações físicas.
- Nunca dê diagnósticos médicos. Deixe claro que é uma análise simbólica, não clínica.
- Termine cada resposta com UMA pergunta reflexiva ou convite para o sonhador explorar mais.
- Responda sempre em Português (BR)."""

st.set_page_config(page_title="Intérprete de Sonhos", page_icon="🌙", layout="centered")

st.title("🌙 Intérprete de Sonhos")
st.caption("Uma sessão com Dr. Hermes — psicanalista onírico")

# --- Chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.gemini_history = []

# --- Display chat ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🌙"):
        st.markdown(msg["content"])

# --- Input ---
if prompt := st.chat_input("Conte seu sonho..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # Build Gemini conversation
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-lite",
        system_instruction=SYSTEM_PROMPT,
    )
    chat = model.start_chat(history=st.session_state.gemini_history)

    with st.chat_message("assistant", avatar="🌙"):
        with st.spinner("Dr. Hermes está interpretando..."):
            response = chat.send_message(prompt)
            reply = response.text
        st.markdown(reply)

    # Persist history
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.gemini_history = chat.history

# --- Sidebar ---
with st.sidebar:
    st.header("Sobre o Dr. Hermes")
    st.markdown(
        "Analista onírico treinado nas tradições de **Jung** e **Freud**.\n\n"
        "Compartilhe seu sonho — mesmo fragmentos — e explore o que o inconsciente tenta comunicar."
    )
    st.divider()
    if st.button("🗑️ Nova sessão", use_container_width=True):
        st.session_state.messages = []
        st.session_state.gemini_history = []
        st.rerun()
    st.caption("Análise simbólica — não substitui acompanhamento clínico.")
