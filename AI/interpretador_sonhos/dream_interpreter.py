import streamlit as st




# with st.chat_message("user", avatar="images.jpg"):
#     st.markdown("Sonhei que estava voando sobre marte!")
#     st.metric(label="Dream Size", value=50)
# with st.chat_message("assistant", avatar="sigmund_freud.jpg"):
#     st.markdown("Dahora MEN!")

# prompt =  st.chat_input("Escreva aqui")
# if prompt:
#     with st.chat_message("assistant", avatar="sigmund_freud.jpg"):
#         st.write(f"That is what you said: {prompt}")

# #Cache com session state:


# if "mensagens" not in st.session_state:
#     st.session_state.mensagens = []

# if prompt:
#     st.session_state.mensagens.append(prompt)

# for m in st.session_state.mensagens:
#     st.write(m)

from google import genai
from google.genai import types

gemini = genai.Client(api_key='AIzaSyAhf6AKQXUc49vRF3_75rCR2FPPtXa8ybg')


# chat = gemini.chats.create(model="gemini-3-flash-preview", config=types.GenerateContentConfig(
#     system_instruction="Você é um analista de sonhos. Responda sempre em português"
# ))

# resposta1 = chat.send_message("Sonhei que estava sem dentes!")
# print(resposta1.text)

# resposta2 = chat.send_message("O que pode significar estar sem dentes???")
# print(resposta2.text)

# print(chat.get_history())

SYSTEM_PROMPT = """
Você deve assumir o papel de Sigmund Freud e interpretar sonhos, sempre que possívle associando os aos arquétipos Jungianos e Freudianos, você deve interpretar sonhos com profundidade simbólica, revelando medos, desejos inconscientes, conflitos internos e aspirações

## Diretrizes:
 - Fale em primeiro pessoa, como se fosse Freud.
 - Identifique os arquétipos 
 - Jamais pode ser fornecido dignósticos ou conselhos médicos, ou interpretações que podem por a saúde física e mental do usuário em risco
 - Responda sempre em português
 - Retone sempre uma pergunta reflexiva, para que o usuário possa se aprofundar mais em seu sonho.
""" 

st.set_page_config(page_title="Dream Weaver")
st.title("Sessão com Doctor Freud")
st.caption("Vamos descobrir o que seus sonhos significam...")

if "mensagens" not in st.session_state:
    st.session_state.mensagens= []
    st.session_state.historico_gemini = []

for m in st.session_state.mensagens:
    if m["role"] == "user":
        avatar = "😶‍🌫️"
    else:
        avatar =  "👨‍⚕️"
    with st.chat_message(m["role"], avatar=avatar):
        st.markdown(m["content"])


if prompt := st.chat_input("conte seu sonho"):
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="😶‍🌫️"):
        st.markdown(prompt)

    chat = gemini.chats.create(model="gemini-3-flash-preview", config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
                            history=st.session_state.historico_gemini)

    with st.chat_message("assistant", avatar="👨‍⚕️"):
        with st.spinner("Freud está pensando...."):
            resposta = chat.send_message(prompt)
        st.markdown(resposta.text)

    st.session_state.mensagens.append({'role': "assistant", 'content': resposta.text})
    st.session_state.historico_gemini = chat.get_history()

with st.sidebar:
    st.write(st.session_state.mensagens)
    st.write(st.session_state.historico_gemini)