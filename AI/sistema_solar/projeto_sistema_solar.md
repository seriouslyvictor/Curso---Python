# 🪐 Projeto Guiado — Explorador do Sistema Solar
**Chat com IA por planeta | Módulo de Inteligência Artificial**

| Duração | Pré-requisito | Arquivo de saída |
|---|---|---|
| 2h30 | `bloco_llm.md` completo | `sistema_solar.py` |

---

## Visão Geral do Projeto

Vamos construir um app onde o usuário escolhe um planeta do sistema solar e conversa com um chatbot especialista naquele planeta. Cada planeta tem sua própria conversa — trocar de planeta não apaga o que foi discutido anteriormente.

Este material foi pensado para aula guiada. A ideia é que o professor explique o conceito, mostre um bloco pequeno de código e pare para testar com a turma antes de avançar.

Regras de leitura para este projeto:

- não pule etapas
- não troque nomes de variáveis por versões mais curtas
- não use atalhos que escondem a lógica
- prefira clareza antes de “código elegante”
- mantenha os nomes e comentários em português brasileiro sempre que possível

**O que vamos aprender construindo isso:**

| Conceito | Onde aparece |
|---|---|
| Histórico de conversa multi-turno | Lista que cresce a cada mensagem |
| `system_instruction` aplicado | Cada planeta tem sua própria instrução |
| `st.chat_message` e `st.chat_input` | Interface de chat no Streamlit |
| `st.tabs` | Navegação por planeta |
| `st.session_state` por chave | Histórico separado para cada planeta |

---

## Por que esse projeto?

Antes de escrever uma linha de código, vale entender o que estamos realmente construindo e por que as escolhas de design importam.

> *"Quando você abre o ChatGPT e começa uma conversa nova, ele não lembra nada do que você falou antes. Mas dentro da mesma conversa, ele lembra tudo. Como isso funciona?"*

A resposta é a peça central desse projeto: **histórico de mensagens**. Toda vez que você manda uma nova mensagem, seu app envia para a IA não só a mensagem nova, mas todo o histórico da conversa até aquele ponto. A IA não tem memória própria — você é quem fornece o contexto a cada chamada.

Esse mecanismo simples está por baixo de todo chatbot que existe: ChatGPT, assistentes de atendimento, tutores de IA. Aprender isso aqui, do zero, com código que vocês mesmos escrevem, é aprender o fundamento real.

---

## ETAPA 1 — O problema da falta de memória *(terminal)*

### O que acontece sem histórico

*Crie um arquivo `solar_terminal.py`. Construa junto com os alunos, bloco a bloco.*

```python
from google import genai
from google.genai import types

# A chave identifica o projeto na API.
# Em aula, o professor pode deixar essa chave configurada de forma segura.
GEMINI_API_KEY = "AIza..."
cliente = genai.Client(api_key=GEMINI_API_KEY)
MODEL = "gemini-2.5-flash"
```

Agora faça duas chamadas independentes:

```python
# ── BLOCO 1 — Duas chamadas sem conexão entre elas ──────────────

resposta1 = cliente.models.generate_content(
    model=MODEL,
    contents="Meu nome é Tibúrcio e meu planeta favorito é Marte."
)
print("Resposta 1:", resposta1.text)

resposta2 = cliente.models.generate_content(
    model=MODEL,
    contents="Qual é o meu nome?"
)
print("Resposta 2:", resposta2.text)
```

Rode. A segunda resposta vai dizer algo como *"Não sei seu nome, você não me disse"* ou vai inventar um nome. O modelo não faz a menor ideia do que foi dito na primeira chamada.

> 💡 **Para a turma:** *"É como se cada vez que você ligasse para alguém, a pessoa não lembrasse de nenhuma ligação anterior. Toda chamada à API é independente — o modelo não tem memória entre elas. Então como o ChatGPT lembra da conversa?"*

---

## ETAPA 2 — A solução: lista de histórico *(terminal)*

### O que a API realmente espera

A API do Gemini — assim como qualquer API de LLM — aceita não só uma string simples, mas uma **lista de mensagens**. Cada mensagem tem um `role` (quem falou) e o conteúdo.

Os roles no Gemini são:
- `"user"` — o que o usuário enviou
- `"model"` — o que o modelo respondeu

```python
# Assim o Gemini representa uma conversa:
# - cada mensagem é um dicionário
# - cada dicionário tem um papel (role) e o conteúdo (parts)
conversa = [
    {"role": "user",  "parts": [{"text": "Meu nome é Tibúrcio."}]},
    {"role": "model", "parts": [{"text": "Olá, Tibúrcio! Como posso ajudar?"}]},
    {"role": "user",  "parts": [{"text": "Qual é o meu nome?"}]},
]

# Agora o modelo tem o contexto inteiro — ele "sabe" o nome
resposta = cliente.models.generate_content(model=MODEL, contents=conversa)
print(resposta.text)   # → "Seu nome é Tibúrcio!"
```

Rode e mostre a diferença. Depois explique o mecanismo:

```
CHAMADA 1:
  Enviado → ["Meu nome é Tibúrcio."]
  Recebido → "Olá, Tibúrcio!"

CHAMADA 2:
  Enviado → ["Meu nome é Tibúrcio.",
              "Olá, Tibúrcio!",           ← incluímos a resposta anterior
              "Qual é o meu nome?"]
  Recebido → "Seu nome é Tibúrcio!"
```

> 💡 **O "segredo" de todo chatbot:** A cada nova mensagem, enviamos o histórico inteiro mais a mensagem nova. O modelo lê tudo do começo, gera a resposta, e devolvemos. É isso. Não existe nenhuma magia de memória — é só uma lista que cresce.

---

### Construindo o loop de conversa

Agora vamos construir um chat de verdade no terminal:

```python
# ── BLOCO 2 — Chat com histórico no terminal ────────────────────

historico = []   # lista vazia — vai crescendo a cada troca

print("=== Chat com Gemini ===")
print("(Digite 'sair' para encerrar)\n")

while True:
    mensagem_usuario = input("Você: ").strip()
    
    if mensagem_usuario.lower() == "sair":
        print("Encerrando...")
        break
    
    if not mensagem_usuario:
        continue
    
    # 1. Adicionamos a mensagem do usuário ao histórico
    historico.append({
        "role": "user",
        "parts": [{"text": mensagem_usuario}]
    })
    
    # 2. Mandamos o histórico inteiro para a API
    resposta = cliente.models.generate_content(
        model=MODEL,
        contents=historico
    )
    
    texto_resposta = resposta.text
    
    # 3. Adicionamos a resposta do modelo ao histórico
    historico.append({
        "role": "model",
        "parts": [{"text": texto_resposta}]
    })
    
    print(f"Gemini: {texto_resposta}\n")
```

Rode. Teste:
- *"Meu nome é [nome do aluno]"*
- *"O que é Marte?"*
- *"Qual é o meu nome?"* — vai lembrar

Depois mostre o histórico crescendo:

```python
    # Adicione essa linha dentro do loop para ver o crescimento:
    print(f"[histórico: {len(historico)} mensagens]\n")
```

> ⚠️ **Alerta de custo:** A cada nova mensagem, você reenvia todo o histórico. Uma conversa de 20 trocas envia ~20x mais tokens que uma conversa de 1 troca. É por isso que chatbots profissionais têm limite de contexto e estratégias para comprimir histórico longo.

---

## ETAPA 3 — System prompt por planeta *(terminal)*

### Especialistas diferentes, mesmo modelo

Agora vamos adicionar o `system_instruction` para criar um especialista por planeta. Perceba como o comportamento muda sem alterar nenhuma outra linha do código:

```python
# ── BLOCO 3 — Chat especializado por planeta ────────────────────

# Lista dos planetas que vamos oferecer no menu.
PLANETAS = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter",
            "Saturno", "Urano", "Netuno"]

def criar_instrucao(planeta):
    return f"""Você é um especialista apaixonado pelo planeta {planeta}.
Responda APENAS sobre {planeta} e o sistema solar quando relevante.
Seja preciso scientificamente, mas use linguagem acessível para adolescentes.
Se perguntarem sobre outro planeta, diga que sua especialidade é {planeta}
e ofereça redirecionar a conversa."""


def chat_planeta(planeta):
    """Inicia um chat dedicado a um planeta específico."""
    historico = []
    instrucao = criar_instrucao(planeta)
    
    config = types.GenerateContentConfig(
        system_instruction=instrucao
    )
    
    print(f"\n=== Especialista em {planeta} ===")
    print(f"(Digite 'sair' para voltar ao menu)\n")
    
    while True:
        mensagem = input("Você: ").strip()
        
        if mensagem.lower() == "sair":
            break
        if not mensagem:
            continue
        
        historico.append({
            "role": "user",
            "parts": [{"text": mensagem}]
        })
        
        resposta = cliente.models.generate_content(
            model=MODEL,
            contents=historico,
            config=config
        )
        
        historico.append({
            "role": "model",
            "parts": [{"text": resposta.text}]
        })
        
        print(f"Especialista: {resposta.text}\n")


# ── Menu de seleção de planeta ───────────────────────────────────

print("=== Explorador do Sistema Solar ===\n")
# Escrevemos o menu de forma explícita para facilitar a leitura dos iniciantes.
indice = 1
for planeta in PLANETAS:
    print(f"{indice}. {planeta}")
    indice += 1

while True:
    escolha = input("\nEscolha um planeta (1-8) ou 'sair': ").strip()
    
    if escolha.lower() == "sair":
        break
    
    try:
        indice_planeta = int(escolha) - 1
        if 0 <= indice_planeta < len(PLANETAS):
            chat_planeta(PLANETAS[indice_planeta])
        else:
            print("Número fora do intervalo.")
    except ValueError:
        print("Digite um número.")
```

Rode. Teste a mesma pergunta em dois planetas diferentes — *"Quais são suas características mais interessantes?"* — e observe como as respostas são completamente distintas apesar de usarem o mesmo modelo.

Teste também perguntar sobre Júpiter enquanto está no chat de Marte. A instrução vai fazer o modelo redirecionar.

> 💡 **Ponto de reflexão:** *"O que mudou entre os dois chats? Só o `system_instruction`. O modelo, os parâmetros, o código — tudo igual. Isso é o que torna os LLMs ferramentas tão versáteis: com uma instrução diferente, o mesmo modelo vira um especialista completamente diferente."*

---

## ETAPA 4 — Portando para o Streamlit: widgets de chat *(Streamlit)*

### Os novos widgets: `st.chat_message` e `st.chat_input`

Agora que o chat funciona no terminal, vamos adicionar a interface. Streamlit tem dois widgets feitos especificamente para isso:

**`st.chat_message(role)`** — exibe uma bolha de mensagem com o ícone correto. O `role` pode ser `"user"` (ícone de pessoa) ou `"assistant"` (ícone de robô).

**`st.chat_input(placeholder)`** — barra de input fixada no rodapé da página. Diferente do `st.text_input`, ela só envia quando o usuário pressiona Enter. Retorna a string digitada, ou `None` se nada foi enviado.

```python
import streamlit as st

# Exibe uma bolha de mensagem do usuário
with st.chat_message("user"):
    st.write("Olá! O que é Marte?")

# Exibe uma bolha de resposta da IA
with st.chat_message("assistant"):
    st.write("Marte é o quarto planeta do sistema solar...")

# Input fixado no rodapé — retorna None até o usuário digitar e pressionar Enter
mensagem = st.chat_input("Digite sua mensagem...")
if mensagem:
    st.write(f"Você digitou: {mensagem}")
```

> 💡 **Como `st.chat_input` funciona com o rerun do Streamlit:** Quando o usuário pressiona Enter, o Streamlit reroda o script inteiro. `st.chat_input` retorna a mensagem digitada nessa execução e `None` nas demais. Por isso colocamos `if mensagem:` antes de processar.

---

### Passo 1 — App de 1 planeta para entender a estrutura

*Crie `sistema_solar.py`. Construa em passos, testando a cada adição.*

```python
import streamlit as st
from google import genai
from google.genai import types

# ── Configuração ──────────────────────────────────────────────────
cliente = genai.Client(api_key=st.secrets["GEMINI_KEY"])
MODEL = "gemini-2.5-flash"

# Esta constante guarda o planeta usado no exemplo inicial.
PLANETA = "Marte"

def criar_instrucao(planeta):
    # A instrução de sistema define o papel do modelo antes da conversa começar.
    # Aqui ela transforma o mesmo modelo em um especialista em um planeta.
    return f"""Você é um especialista apaixonado pelo planeta {planeta}.
Responda APENAS sobre {planeta} e o sistema solar quando relevante.
Seja preciso cientificamente, mas use linguagem acessível para adolescentes.
Se perguntarem sobre outro planeta, diga que sua especialidade é {planeta}."""

# ── Interface ─────────────────────────────────────────────────────
st.title(f"🔴 Especialista em {PLANETA}")

# Inicializa o histórico na primeira execução
if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibe todas as mensagens do histórico
for mensagem in st.session_state.historico:
    role_display = "user" if mensagem["role"] == "user" else "assistant"
    with st.chat_message(role_display):
        st.write(mensagem["parts"][0]["text"])

# Input do usuário — fica fixo no rodapé
entrada = st.chat_input(f"Pergunte sobre {PLANETA}...")

if entrada:
    # 1. Mostra a mensagem do usuário imediatamente
    with st.chat_message("user"):
        st.write(entrada)
    
    # 2. Adiciona ao histórico
    st.session_state.historico.append({
        "role": "user",
        "parts": [{"text": entrada}]
    })
    
    # 3. Chama a API com o histórico inteiro
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            config = types.GenerateContentConfig(
                system_instruction=criar_instrucao(PLANETA)
            )
            resposta = cliente.models.generate_content(
                model=MODEL,
                contents=st.session_state.historico,
                config=config
            )
            texto = resposta.text
        
        st.write(texto)
    
    # 4. Adiciona a resposta ao histórico
    st.session_state.historico.append({
        "role": "model",
        "parts": [{"text": texto}]
    })
```

Rode. Teste uma conversa de 3-4 mensagens. Mostre que o histórico persiste entre reruns. Mostre que o `session_state.historico` é exatamente a mesma lista que construímos no terminal — nada mudou conceitualmente, só a exibição.

---

## ETAPA 5 — `st.tabs` e histórico por planeta *(Streamlit)*

### O problema que surge naturalmente

Se usarmos um único `historico` no `session_state` e trocamos de planeta no meio da conversa, acontece isso:

```
[Aba Marte]    Usuário: "Qual é a temperatura em Marte?"
[Aba Marte]    Especialista: "A temperatura média em Marte é -60°C..."
[Aba Júpiter]  Usuário: "Você tem alguma lua?"
[Aba Júpiter]  Especialista: "Sim! Phobos e Deimos..." ← ERRADO — isso é Marte
```

O histórico de Marte contamina a conversa de Júpiter. A solução é guardar um histórico separado por planeta no `session_state`.

> 💡 **Esse é um problema de arquitetura real.** Qualquer app com múltiplos contextos precisa resolver exatamente isso. A solução aqui — usar chaves diferentes no `session_state` — é o mesmo padrão que você usaria num sistema profissional.

---

### Passo 2 — Múltiplas abas com histórico separado

```python
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
```

Rode. Teste:
1. Faça uma pergunta na aba Marte
2. Vá para a aba Júpiter e faça outra pergunta
3. Volte para Marte — a conversa anterior está lá
4. Continue a conversa de Marte — o modelo lembra do contexto

> 💡 **Por que `key=f"input_{planeta}"` no `st.chat_input`?** Streamlit exige que widgets interativos numa mesma página tenham chaves únicas. Como vamos criar 8 `st.chat_input` (um por aba), cada um precisa de uma chave diferente. Sem isso, o Streamlit lança um erro.

---

### Entendendo `st.tabs`

```python
# st.tabs() recebe uma lista de strings — essas são as etiquetas das abas
abas = st.tabs(["Aba 1", "Aba 2", "Aba 3"])

# Retorna uma lista de contextos — um por aba
# Você usa "with aba:" para colocar conteúdo dentro de uma aba específica
with abas[0]:
    st.write("Conteúdo da primeira aba")

with abas[1]:
    st.write("Conteúdo da segunda aba")

# Ou com uma repetição explícita, que costuma ser mais fácil para iniciantes:
dados = ["Dado A", "Dado B", "Dado C"]
for indice in range(len(abas)):
    with abas[indice]:
        st.write(dados[indice])
```

---

## Código Completo — `sistema_solar.py`

*Para referência — não cole direto. Construa junto com os alunos chegando aqui organicamente.*

```python
import streamlit as st
from google import genai
from google.genai import types

# ── Configuração ──────────────────────────────────────────────────
cliente = genai.Client(api_key=st.secrets["GEMINI_KEY"])
MODEL = "gemini-2.5-flash"

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
    return f"historico_{planeta.lower()}"

def inicializar_historico(planeta):
    chave = chave_historico(planeta)
    if chave not in st.session_state:
        st.session_state[chave] = []

def renderizar_chat(planeta):
    inicializar_historico(planeta)
    chave = chave_historico(planeta)
    
    for mensagem in st.session_state[chave]:
        role_display = "user" if mensagem["role"] == "user" else "assistant"
        with st.chat_message(role_display):
            st.write(mensagem["parts"][0]["text"])
    
    entrada = st.chat_input(
        f"Pergunte sobre {planeta}...",
        key=f"input_{planeta}"
    )
    
    if entrada:
        with st.chat_message("user"):
            st.write(entrada)
        
        st.session_state[chave].append({
            "role": "user",
            "parts": [{"text": entrada}]
        })
        
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
        
        st.session_state[chave].append({
            "role": "model",
            "parts": [{"text": texto}]
        })

# ── Interface ─────────────────────────────────────────────────────
st.title("🪐 Explorador do Sistema Solar")
st.write("Escolha um planeta e converse com seu especialista dedicado.")

abas = st.tabs(list(PLANETAS.keys()))

nomes_abas = list(PLANETAS.keys())
for indice in range(len(nomes_abas)):
    planeta = PLANETAS[nomes_abas[indice]]
    with abas[indice]:
        renderizar_chat(planeta)
```

---

## Desafios Progressivos

### 🎯 Nível 1 — Botão de limpar conversa *(~10 min)*

> Adicione dentro de cada aba um botão "🗑️ Limpar conversa" que zera o histórico daquele planeta sem afetar os outros.
>
> **Dica:** `st.session_state[chave_historico(planeta)] = []`
>
> ✅ Critério: limpar Marte não afeta a conversa de Júpiter.

---

### 🎯 Nível 2 — Curiosidade do dia *(~20 min)*

> Ao abrir cada aba pela primeira vez (histórico vazio), exiba automaticamente uma curiosidade sobre aquele planeta gerada pela IA, sem precisar que o usuário pergunte nada.
>
> **Dica:** verifique se `len(st.session_state[chave]) == 0` e, se sim, faça uma chamada automática pedindo uma curiosidade surpreendente sobre o planeta.
>
> ✅ Critério: ao trocar de aba em um planeta nunca visitado, uma curiosidade aparece automaticamente.

---

### 🎯 Nível 3 — Personalidade dramática *(~15 min)*

> Crie uma versão alternativa onde **o planeta fala em primeira pessoa** — como se fosse o próprio planeta sendo entrevistado, com personalidade e drama.
>
> **Exemplo de instrução:**
> *"Você É o planeta Marte. Fale em primeira pessoa, com personalidade orgulhosa e dramática. Mencione sua cor vermelha como algo nobre. Refira-se aos humanos como 'os terrícolas'. Seja científico mas teatral."*
>
> Adicione um `st.toggle("🎭 Modo dramático")` no topo do app que alterna entre as duas instruções.
>
> ✅ Critério: o toggle muda o comportamento do chatbot visivelmente nas próximas respostas.

---

### 🎯 Nível 4 — Contador de tokens por planeta *(~25 min)*

> Adicione no sidebar um painel mostrando quantos tokens foram consumidos em cada planeta durante a sessão.
>
> **Dica:** guarde também `st.session_state[f"tokens_{planeta}"]` e some `resposta.usage_metadata.total_token_count` a cada resposta.
>
> Exiba com `st.sidebar.metric()` e um total geral no rodapé do sidebar.
>
> ✅ Critério: os tokens acumulam por planeta e o total é a soma de todos.

---

## Expansões Naturais — Para Quem Terminar Cedo

O projeto foi desenhado para crescer com uma linha de código. Mostre essas ideias para a turma e deixe quem terminar cedo explorar:

```python
# Trocar planetas por qualquer outra coisa — mesma estrutura, zero mudança arquitetural:

# Períodos históricos
TEMAS = {"🏛️ Roma Antiga": "Roma Antiga", "⚔️ Idade Média": "Idade Média", ...}

# Linguagens de programação
TEMAS = {"🐍 Python": "Python", "☕ Java": "Java", "🦀 Rust": "Rust", ...}

# Personagens mitológicos — cada deus responde em primeira pessoa
TEMAS = {"⚡ Zeus": "Zeus", "💀 Hades": "Hades", "🔱 Poseidon": "Poseidon", ...}
```

> 💡 **Ponto para a turma:** *"O que mudou entre o app de planetas e o de deuses gregos? Só o dicionário `PLANETAS` e o texto da instrução. A arquitetura — o histórico por chave, as abas, o chat — é exatamente a mesma. Isso é o que acontece quando você escreve código bem estruturado."*

---

## Referência Rápida — Widgets de Chat

| Widget | Para que serve | Retorna |
|---|---|---|
| `st.chat_message("user")` | Bolha com ícone de pessoa | context manager |
| `st.chat_message("assistant")` | Bolha com ícone de robô | context manager |
| `st.chat_input("placeholder", key=...)` | Input fixo no rodapé | `str` ou `None` |
| `st.tabs(["A", "B", "C"])` | Lista de abas clicáveis | lista de context managers |

---

## Referência Rápida — Padrão de Histórico Gemini

```python
# Estrutura de uma mensagem no histórico
mensagem_usuario = {
    "role": "user",
    "parts": [{"text": "Sua mensagem aqui"}]
}

mensagem_modelo = {
    "role": "model",
    "parts": [{"text": "Resposta do modelo aqui"}]
}

# Inicialização
historico = []

# Adicionar mensagem do usuário
historico.append({"role": "user", "parts": [{"text": entrada}]})

# Chamar API com histórico
resposta = cliente.models.generate_content(
    model=MODEL,
    contents=historico,
    config=types.GenerateContentConfig(system_instruction="...")
)

# Adicionar resposta ao histórico
historico.append({"role": "model", "parts": [{"text": resposta.text}]})

# No Streamlit: histórico por entidade usando session_state
chave = f"historico_{nome_entidade.lower()}"
if chave not in st.session_state:
    st.session_state[chave] = []
```
