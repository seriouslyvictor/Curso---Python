# 🌙 Bloco de Aula — Intérprete de Sonhos com Streamlit e Gemini
**Chat com IA | st.chat_message · st.chat_input · st.session_state**

| Duração | Público | Pré-requisito |
|---|---|---|
| ~2h | Ensino médio público, adolescentes | Bloco TMDB concluído · `st.button`, `st.spinner`, `st.session_state` básico |

---

## Visão Geral do Bloco

| Etapa | Tema | Duração |
|---|---|---|
| 1 | Por que um chat é diferente de um formulário? | 15 min |
| 2 | Os widgets de chat do Streamlit | 20 min |
| 3 | `st.session_state` a fundo — a memória do app | 20 min |
| 4 | O novo SDK do Gemini (`google-genai`) | 20 min |
| 5 | Construção guiada: Dr. Hermes | 30 min |
| 6 | Mini-desafios | 15 min |

---

## Por que um chat é diferente de um formulário?

Até agora todos os nossos apps seguiam o mesmo roteiro: usuário preenche um campo, clica em um botão, app mostra um resultado. Fim. O app não lembra de nada — se você clicar no botão de novo, é como se a conversa anterior nunca tivesse existido.

Um chat é diferente. Ele tem **histórico**. A mensagem que você manda agora faz referência às anteriores — o Dr. Hermes precisa lembrar que você já mencionou "um corredor escuro" antes de poder aprofundar a análise do símbolo.

Esse problema tem dois lados:

**Lado 1 — O Streamlit reroda tudo a cada interação.** Toda vez que o usuário manda uma mensagem, o Python executa o arquivo do zero. As variáveis somem. A solução é o `st.session_state`, que aprendemos antes — mas agora vamos usá-lo de verdade, de forma mais sofisticada.

**Lado 2 — A IA não tem memória entre chamadas.** Cada vez que fazemos uma chamada para o Gemini, ele não sabe nada do que aconteceu antes a não ser que a gente mande o histórico junto. É exatamente como mandar uma carta nova para alguém — sem o contexto anterior, a pessoa não sabe do que você está falando.

A solução para os dois problemas é a mesma: guardar o histórico da conversa no `st.session_state` e repassá-lo para o Gemini a cada nova mensagem.

---

## ETAPA 1 — Os Widgets de Chat do Streamlit (20 min)

### `st.chat_message()` — a bolha de mensagem

```python
import streamlit as st

# Bolha do usuário
with st.chat_message("user"):
    st.markdown("Sonhei que estava voando sobre uma cidade afundada.")

# Bolha do assistente
with st.chat_message("assistant"):
    st.markdown("Fascinante. Cidades submersas frequentemente representam...")
```

O parâmetro aceita `"user"` ou `"assistant"` — o Streamlit já define a posição e a cor automaticamente. Você pode passar um emoji como avatar:

```python
with st.chat_message("user", avatar="🧑"):
    st.markdown("Olá!")

with st.chat_message("assistant", avatar="🌙"):
    st.markdown("Bem-vindo à sessão.")
```

> 💡 **Mostre ao vivo:** cole o código acima, rode, mostre as duas bolhas lado a lado. Pergunte aos alunos: "O que acontece se eu adicionar `st.metric()` dentro de `st.chat_message()`?" (Funciona — qualquer widget pode entrar dentro de uma bolha.)

---

### `st.chat_input()` — o campo que fica fixo no rodapé

```python
import streamlit as st

prompt = st.chat_input("Escreva aqui...")

if prompt:
    st.write(f"Você disse: {prompt}")
```

Diferente do `st.text_input()`, o `st.chat_input()` sempre aparece fixado na parte inferior da tela, como o WhatsApp. Ao apertar Enter ou clicar na setinha, o campo dispara — sem precisar de `st.button()`.

**A rasteira clássica:** `st.chat_input()` retorna `None` quando vazio e a string digitada quando o usuário envia. Por isso usamos `if prompt:` — exatamente o mesmo padrão do `if st.button()`.

> ⚠️ **Só pode haver um `st.chat_input()` por app.** Se você colocar dois, o Streamlit vai reclamar.

---

### O padrão de exibição do histórico

O fluxo de todo app de chat segue sempre a mesma ordem:

```
1. Exibir o histórico que já existe  ← primeiro!
2. Pegar o novo input do usuário
3. Exibir a nova mensagem do usuário
4. Chamar a IA
5. Exibir a resposta da IA
6. Salvar tudo no histórico
```

**Por que exibir primeiro?** Porque o Streamlit reroda o script do zero. Se você não exibir o histórico logo no começo, ele some a cada interação.

---

## ETAPA 2 — `st.session_state` a Fundo (20 min)

### O problema que ele resolve

Rode esse código e abra no navegador:

```python
import streamlit as st

mensagens = []  # lista comum — morre a cada rerun

prompt = st.chat_input("Diga algo...")
if prompt:
    mensagens.append(prompt)

for msg in mensagens:
    st.write(msg)
```

Mande uma mensagem. Mande outra. A lista sempre tem só a última. As anteriores sumiram porque o Python recriou `mensagens = []` do zero.

Agora a versão que funciona:

```python
import streamlit as st

# Inicialização segura — só cria a lista se ela ainda não existe
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Exibe o histórico ANTES de pegar o novo input
for msg in st.session_state.mensagens:
    st.write(msg)

prompt = st.chat_input("Diga algo...")
if prompt:
    st.session_state.mensagens.append(prompt)
    st.rerun()  # força o rerun para exibir a mensagem nova no histórico
```

> 💡 **Explique o `if "mensagens" not in st.session_state`:** na primeira execução, a chave não existe — então criamos. Nas execuções seguintes, ela já existe e nós não zeramos. É exatamente como um guarda-volume: na primeira vez você entrega a mochila, depois só pega ela de volta.

---

### Guardando dicionários no histórico

Para um chat de verdade, cada mensagem precisa de dois campos: quem falou (`role`) e o que foi dito (`content`). Guardamos como uma lista de dicionários:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Novo input
prompt = st.chat_input("Sua mensagem...")
if prompt:
    # 1. Adiciona ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 2. Exibe imediatamente (sem esperar rerun)
    with st.chat_message("user"):
        st.markdown(prompt)
    # 3. Aqui virá a chamada para a IA...
```

> 💡 **Mostre a estrutura do `st.session_state` no terminal:** adicione `st.write(st.session_state)` temporariamente para os alunos verem o dicionário crescendo a cada mensagem. Isso torna o conceito concreto.

---

### Dois históricos em paralelo

Nosso app vai precisar manter **dois** históricos no `session_state`:

| Variável | Para que serve | Formato |
|---|---|---|
| `st.session_state.messages` | Exibir as bolhas na tela | Lista de `{"role": ..., "content": ...}` |
| `st.session_state.gemini_history` | Passar contexto para a IA | Lista de objetos `Content` do SDK do Gemini |

São dois formatos diferentes porque o Streamlit fala uma língua e o Gemini fala outra. A gente mantém os dois sincronizados.

---

## ETAPA 3 — O Novo SDK do Gemini (20 min)

### Por que o código mudou?

O app original usava `import google.generativeai as genai` — o SDK antigo, que o Google já está descontinuando. O novo pacote se chama `google-genai` e o import mudou para `from google import genai`. A lógica é a mesma, mas a sintaxe é diferente.

**Instale o pacote novo:**
```bash
pip install google-genai
```

> ⚠️ Se você tiver o antigo instalado (`google-generativeai`), os dois podem coexistir, mas o import é diferente. Para este projeto use sempre `from google import genai`.

---

### Comparação: antes e depois

| Operação | SDK antigo (`google-generativeai`) | SDK novo (`google-genai`) |
|---|---|---|
| Import | `import google.generativeai as genai` | `from google import genai` |
| Criar cliente | `genai.configure(api_key=...)` | `client = genai.Client(api_key=...)` |
| Criar modelo | `genai.GenerativeModel(model_name=..., system_instruction=...)` | Vai dentro do `config` do chat |
| Iniciar chat | `model.start_chat(history=...)` | `client.chats.create(model=..., config=..., history=...)` |
| Enviar mensagem | `chat.send_message(prompt)` | `chat.send_message(prompt)` ✓ igual |
| Ler resposta | `response.text` | `response.text` ✓ igual |
| Pegar histórico | `chat.history` | `chat.get_history()` |

---

### Hello World com o novo SDK

```python
from google import genai
from google.genai import types

# O cliente lê GEMINI_API_KEY automaticamente do ambiente,
# ou você pode passar: genai.Client(api_key="sua_chave")
client = genai.Client(api_key="sua_chave_aqui")

resposta = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Me explique o que é um arquétipo junguiano em 2 frases."
)

print(resposta.text)
```

---

### Chat com system instruction e histórico

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="sua_chave_aqui")

# Criamos o chat passando:
# - model: qual modelo usar
# - config: configurações, incluindo a instrução de sistema
# - history: o histórico de mensagens anteriores (vazio no início)
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="Você é um analista de sonhos. Responda sempre em português."
    ),
    history=[]  # começa vazio, preenchemos nas próximas rodadas
)

# Enviando mensagens
resposta1 = chat.send_message("Sonhei que eu voava.")
print(resposta1.text)

resposta2 = chat.send_message("O que o voo pode significar?")
print(resposta2.text)

# Pegando o histórico para guardar no session_state
historico = chat.get_history()
print(f"Total de mensagens no histórico: {len(historico)}")
```

> 💡 **Explique o `history=[]`:** na primeira mensagem, não temos histórico. Depois de cada resposta, chamamos `chat.get_history()` e salvamos o resultado no `session_state`. Na próxima vez que o Streamlit roda o script, criamos um novo chat passando esse histórico salvo — e a IA "lembra" de tudo.

---

### Modelos disponíveis e quando usar cada um

| Modelo | Quando usar | Custo relativo |
|---|---|---|
| `gemini-3.1-flash-lite` | Testes, prototipagem, alto volume | ⭐ Mais barato |
| `gemini-3-flash-preview` | Projetos finais, qualidade equilibrada | ⭐⭐ Médio |
| `gemini-3.1-pro-preview` | Máxima qualidade, tarefas complexas | ⭐⭐⭐ Mais caro |

Para este projeto, `gemini-3-flash-preview` é a escolha certa.

---

## ETAPA 4 — Construção Guiada: Dr. Hermes (30 min)

### O que vamos construir

Um chat com um psicanalista fictício especializado em sonhos. Ele usa conceitos junguianos e freudianos para interpretar o que o usuário conta, faz perguntas reflexivas e mantém o contexto de toda a conversa.

*Construa junto com os alunos. Um passo por vez, testando a cada adição.*

---

### Passo 1 — Estrutura básica e system prompt

Crie `interprete_sonhos.py`:

```python
import streamlit as st
from google import genai
from google.genai import types

# ─────────────────────────────────────────────
# SYSTEM PROMPT — define a personalidade da IA
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """Você é Dr. Hermes — um psicanalista onírico fictício formado
na tradição junguiana e freudiana.
Sua missão é interpretar sonhos com profundidade simbólica, revelando arquétipos,
desejos inconscientes e conflitos internos.

Diretrizes:
- Fale em primeira pessoa, com tom solene mas acessível.
- Identifique arquétipos junguianos (Sombra, Anima/Animus, Self, Trickster...)
  quando relevantes.
- Aplique leitura freudiana com parcimônia.
- Nunca dê diagnósticos médicos. Deixe claro que é análise simbólica.
- Termine cada resposta com UMA pergunta reflexiva.
- Responda sempre em Português (BR)."""

st.set_page_config(page_title="Intérprete de Sonhos", page_icon="🌙", layout="centered")
st.title("🌙 Intérprete de Sonhos")
st.caption("Uma sessão com Dr. Hermes — psicanalista onírico")
```

Rode. Veja o título e o caption aparecerem. A tela está vazia — sem histórico, sem input ainda.

---

### Passo 2 — Inicializar o `session_state`

Logo abaixo do `st.caption()`:

```python
# ─────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# Roda apenas na primeira execução do script.
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []        # histórico para exibir na tela
    st.session_state.gemini_history = []  # histórico para passar à IA
```

> 💡 **Explique o porquê de dois históricos:** `messages` usa dicionários simples com `role` e `content` — o Streamlit entende. `gemini_history` usa os objetos `Content` do SDK — o Gemini entende. São dois "idiomas" diferentes para o mesmo conteúdo.

---

### Passo 3 — Exibir o histórico existente

```python
# ─────────────────────────────────────────────
# EXIBIÇÃO DO HISTÓRICO
# Sempre ANTES do st.chat_input — isso é crítico!
# ─────────────────────────────────────────────
for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "🌙"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
```

Rode. A tela ainda está vazia porque o histórico está vazio. Isso é correto.

---

### Passo 4 — Receber a mensagem do usuário

```python
# ─────────────────────────────────────────────
# INPUT DO USUÁRIO
# st.chat_input retorna None enquanto vazio
# e a string da mensagem quando enviado.
# ─────────────────────────────────────────────
if prompt := st.chat_input("Conte seu sonho..."):

    # 1. Adiciona ao histórico de exibição
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Exibe a bolha do usuário imediatamente
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
```

> 💡 **Explique o `if prompt := st.chat_input(...)`:** isso é chamado de *walrus operator* (`:=`). Ele faz duas coisas ao mesmo tempo: atribui o resultado do `st.chat_input()` à variável `prompt` E testa se é `True` (ou seja, se o usuário de fato enviou algo). É um atalho — equivale a:
> ```python
> prompt = st.chat_input("Conte seu sonho...")
> if prompt:
> ```

---

### Passo 5 — Chamar a IA e exibir a resposta

Dentro do `if prompt`:

```python
    # 3. Cria o cliente e o chat, passando o histórico salvo
    client = genai.Client(api_key=st.secrets["GEMINI_KEY"])

    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        ),
        history=st.session_state.gemini_history  # contexto acumulado
    )

    # 4. Envia a mensagem e exibe a resposta na bolha do assistente
    with st.chat_message("assistant", avatar="🌙"):
        with st.spinner("Dr. Hermes está interpretando..."):
            response = chat.send_message(prompt)
            reply = response.text
        st.markdown(reply)

    # 5. Persiste os dois históricos
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.gemini_history = chat.get_history()
```

> 💡 **Por que recriamos o `chat` a cada rerun?** O Streamlit não "lembra" de objetos Python entre execuções — só o `session_state` persiste. Por isso, a cada mensagem nova criamos um chat "do zero", mas passamos o `gemini_history` salvo. O Gemini recebe todo o contexto e continua a conversa de onde parou.

---

### Passo 6 — Sidebar com botão de nova sessão

```python
# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("Sobre o Dr. Hermes")
    st.markdown(
        "Analista onírico treinado nas tradições de **Jung** e **Freud**.\n\n"
        "Compartilhe seu sonho — mesmo fragmentos — e explore o que o "
        "inconsciente tenta comunicar."
    )
    st.divider()
    if st.button("🗑️ Nova sessão", use_container_width=True):
        st.session_state.messages = []
        st.session_state.gemini_history = []
        st.rerun()
    st.caption("Análise simbólica — não substitui acompanhamento clínico.")
```

> 💡 **Explique o `st.rerun()`:** ao zeramos o `session_state`, o Streamlit não re-executa o script sozinho — ele ainda está no meio do clique do botão. O `st.rerun()` força uma nova execução imediata, e aí sim a tela aparece limpa.

---

### Código completo — `interprete_sonhos.py`

```python
import streamlit as st
from google import genai
from google.genai import types

# ── Config ──────────────────────────────────────
SYSTEM_PROMPT = """Você é Dr. Hermes — um psicanalista onírico fictício formado
na tradição junguiana e freudiana.
Sua missão é interpretar sonhos com profundidade simbólica, revelando arquétipos,
desejos inconscientes e conflitos internos.

Diretrizes:
- Fale em primeira pessoa, com tom solene mas acessível.
- Identifique arquétipos junguianos (Sombra, Anima/Animus, Self, Trickster...)
  quando relevantes.
- Aplique leitura freudiana com parcimônia.
- Nunca dê diagnósticos médicos. Deixe claro que é análise simbólica.
- Termine cada resposta com UMA pergunta reflexiva.
- Responda sempre em Português (BR)."""

st.set_page_config(page_title="Intérprete de Sonhos", page_icon="🌙", layout="centered")
st.title("🌙 Intérprete de Sonhos")
st.caption("Uma sessão com Dr. Hermes — psicanalista onírico")

# ── Session State ────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.gemini_history = []

# ── Exibir Histórico ─────────────────────────────
for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "🌙"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ── Input ─────────────────────────────────────────
if prompt := st.chat_input("Conte seu sonho..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    client = genai.Client(api_key=st.secrets["GEMINI_KEY"])
    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        ),
        history=st.session_state.gemini_history
    )

    with st.chat_message("assistant", avatar="🌙"):
        with st.spinner("Dr. Hermes está interpretando..."):
            response = chat.send_message(prompt)
            reply = response.text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.gemini_history = chat.get_history()

# ── Sidebar ───────────────────────────────────────
with st.sidebar:
    st.header("Sobre o Dr. Hermes")
    st.markdown(
        "Analista onírico treinado nas tradições de **Jung** e **Freud**.\n\n"
        "Compartilhe seu sonho — mesmo fragmentos — e explore o que o "
        "inconsciente tenta comunicar."
    )
    st.divider()
    if st.button("🗑️ Nova sessão", use_container_width=True):
        st.session_state.messages = []
        st.session_state.gemini_history = []
        st.rerun()
    st.caption("Análise simbólica — não substitui acompanhamento clínico.")
```

---

### `secrets.toml` para a chave do Gemini

```toml
# .streamlit/secrets.toml
GEMINI_KEY = "AIza..."
```

No código, acesse com `st.secrets["GEMINI_KEY"]`. No Streamlit Cloud, configure pelo painel web — a chave nunca vai para o GitHub.

---

## Mapa Mental do Fluxo Completo

```
PRIMEIRO ACESSO
    └── session_state criado (messages=[], gemini_history=[])
    └── histórico exibido (nada para mostrar)
    └── st.chat_input aguardando...

USUÁRIO ENVIA MENSAGEM
    └── messages.append({"role":"user", "content": prompt})
    └── bolha do usuário exibida
    └── client.chats.create(history=gemini_history)  ← contexto acumulado
    └── chat.send_message(prompt)
    └── bolha do assistente exibida
    └── messages.append({"role":"assistant", "content": reply})
    └── gemini_history = chat.get_history()  ← salva para próxima rodada

PRÓXIMA MENSAGEM
    └── Streamlit reroda o script DO ZERO
    └── session_state ainda existe  ← aqui está a mágica
    └── histórico exibido (mostra toda a conversa)
    └── novo chat criado com o gemini_history salvo
    └── ciclo se repete...

BOTÃO "NOVA SESSÃO"
    └── messages = []
    └── gemini_history = []
    └── st.rerun()  ← tela limpa
```

---

## ETAPA 5 — Mini-Desafios (15 min)

### 🎯 Desafio 1 — Contador de mensagens *(fácil)*

> Adicione no sidebar um `st.metric()` mostrando quantas mensagens já foram trocadas nessa sessão.
>
> **Dica:** `len(st.session_state.messages)` já tem a resposta.
>
> ✅ Critério: o número atualiza a cada mensagem enviada.

---

### 🎯 Desafio 2 — Mensagem de boas-vindas automática *(médio)*

> Quando a sessão está vazia (sem mensagens), exiba automaticamente uma mensagem do Dr. Hermes na bolha do assistente, convidando o usuário a contar um sonho.
>
> **Dica:** use `if not st.session_state.messages:` antes do loop de exibição. Essa mensagem não deve entrar no histórico real.
>
> ✅ Critério: a mensagem de boas-vindas aparece apenas quando a conversa está vazia.

---

### 🎯 Desafio 3 — Mudar o analista *(difícil)*

> Adicione no sidebar um `st.selectbox` com pelo menos 3 "analistas" diferentes, cada um com um system prompt distinto (ex: "Analista Junguiano", "Analista Freudiano", "Analista Lacaniano"). Quando o usuário trocar de analista, a sessão deve reiniciar automaticamente.
>
> **Dica:** salve o analista atual em `st.session_state.analista` e compare com o valor do `selectbox` a cada rerun. Se mudou, chame `st.rerun()`.
>
> ✅ Critério: cada analista tem uma voz diferente e trocar de analista limpa o histórico.

---

## Referência Rápida — Widgets de Chat

| Widget | O que faz | Retorna |
|---|---|---|
| `st.chat_input(placeholder)` | Campo fixo no rodapé | `str` ou `None` |
| `st.chat_message("user")` | Bolha à direita | context manager |
| `st.chat_message("assistant")` | Bolha à esquerda | context manager |
| `st.session_state.X` | Persiste entre reruns | qualquer tipo Python |
| `st.rerun()` | Força nova execução imediata | — |

---

## Referência Rápida — Novo SDK do Gemini

```python
from google import genai
from google.genai import types

# 1. Criar cliente (lê GEMINI_API_KEY do ambiente ou de st.secrets)
client = genai.Client(api_key=st.secrets["GEMINI_KEY"])

# 2. Criar chat com system instruction e histórico
chat = client.chats.create(
    model="gemini-3-flash-preview",          # ou "gemini-3.1-flash-lite" para economizar
    config=types.GenerateContentConfig(
        system_instruction="Sua persona aqui..."
    ),
    history=st.session_state.gemini_history  # [] na primeira vez
)

# 3. Enviar mensagem e ler resposta
response = chat.send_message("mensagem do usuário")
texto = response.text

# 4. Salvar histórico para a próxima rodada
st.session_state.gemini_history = chat.get_history()
```

---

## Perguntas para Discussão em Aula

- **Por que não podemos guardar o objeto `chat` diretamente no `session_state`?**
  *(Resposta: objetos de conexão com APIs geralmente não são serializáveis — é mais seguro guardar só os dados e recriar o objeto.)*

- **O que aconteceria se o histórico ficasse muito longo?** Como resolver?
  *(Resposta: a API começa a cobrar mais tokens e fica mais lenta. Solução: limitar com `st.session_state.gemini_history[-10:]` para guardar só as últimas mensagens.)*

- **Qual a diferença entre `st.session_state` e um arquivo `.json`?**
  *(Resposta: `session_state` existe só enquanto o navegador está aberto — fecha o navegador, perdeu. JSON persiste entre sessões.)*

---

*Bloco elaborado para turmas do ensino médio público — foco em compreensão do fluxo de chat com IA antes de qualquer personalização visual.*
