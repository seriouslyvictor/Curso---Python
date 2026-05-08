# 🤖 Plano de Aula — Inteligência Artificial e LLMs com Python
**Do ChatGPT ao Backend: Entendendo e Integrando Modelos de Linguagem | Curso Python Generalista**

| Duração total | Público | Pré-requisito |
|---|---|---|
| 5 horas | Ensino médio público, adolescentes | Funções, `requests`, Streamlit básico, conceito de API |

---

## Visão Geral da Aula

| Bloco | Tema | Duração |
|---|---|---|
| 1 | O que é um LLM? Tokens, contexto e como tudo funciona | 1h |
| 2 | O mercado de IA: provedores, modelos e o custo real | 1h |
| 3 | Primeira chamada manual à API (sem SDK) | 45min |
| 4 | SDKs: a camada de abstração que facilita tudo | 45min |
| 5 | Gemini no curso: configuração e primeiros experimentos | 1h30 |

---

## Por que aprender isso agora?

### A conversa honesta antes de começar

Vocês já usaram ChatGPT, Gemini, ou algum outro assistente de IA. Provavelmente mais de uma vez hoje. Mas existe uma diferença fundamental entre *usar* uma IA e *construir* algo com ela — e essa diferença é exatamente o que separa um usuário de um desenvolvedor.

Quando você abre o ChatGPT e digita uma pergunta, você está usando uma *interface* que alguém construiu. Por baixo dessa interface existe uma API — um serviço que qualquer pessoa pode acessar programaticamente para criar seus próprios produtos. É essa API que vamos aprender a usar.

Com isso, vocês vão conseguir:

- Criar um app que analisa imagens e gera texto automaticamente
- Fazer uma ferramenta que responde perguntas sobre um PDF
- Construir um chatbot personalizado para qualquer finalidade
- Integrar IA em qualquer projeto que já sabem fazer

> *"A IA não vai substituir você. Mas uma pessoa que sabe usar IA vai substituir quem não sabe."*

Essa frase circula muito no mercado de tecnologia. Independente de ser verdade ou não, o fato é que saber integrar IA em software é hoje uma habilidade com altíssima demanda e pouquíssima oferta — especialmente entre pessoas novas no mercado.

### Como conduzir esta aula

Este plano foi escrito para professor e turma trabalharem juntos. O melhor ritmo é:

- explicar o conceito em português simples
- mostrar um bloco pequeno de código
- pedir que os alunos digam o que cada linha faz
- testar antes de seguir para o próximo passo

Nesta aula, a preferência é por lógica explícita e leitura fácil. Evite abreviações desnecessárias, não use comprehensions ainda e não troque clareza por truques de sintaxe.

---

## BLOCO 1 — O que é um LLM? (1h)

### Objetivo
O aluno consegue explicar em suas próprias palavras o que é um LLM, o que são tokens, e por que o tamanho do contexto importa. Entende a diferença entre usar um chat (interface) e chamar uma API (backend).

---

### 1.1 A metáfora do autocomplete turbinado

Todos já viram o autocomplete do celular — você começa a digitar e ele sugere a próxima palavra. Um LLM (**Large Language Model**, Modelo de Linguagem Grande) faz essencialmente a mesma coisa, mas numa escala absurdamente maior.

Ele foi treinado em quantidades gigantescas de texto — livros, artigos, código, conversas — e aprendeu padrões. Dado um texto de entrada, ele calcula qual é a sequência de palavras mais provável para continuar aquele texto.

A diferença para o autocomplete do celular é que:
- O LLM viu muito mais texto durante o treinamento
- Ele consegue manter coerência por textos muito mais longos
- Ele aprendeu padrões sofisticados o suficiente para parecer que está "entendendo" e "raciociando"

> 💡 **Para discussão em aula:** *"O ChatGPT realmente entende o que a gente fala, ou ele só está fazendo autocomplete muito bem feito?"* — Não existe resposta certa. É uma das perguntas mais debatidas em IA atualmente. O importante é saber que o mecanismo interno é previsão de próximos tokens, mesmo que o resultado pareça compreensão.

---

### 1.2 O que é um token?

Token é a unidade com que os LLMs processam texto. **Não é uma letra, não é uma palavra — é algo no meio do caminho.**

Na prática, você pode pensar em token como um pedaço de palavra. A regra geral: **1 token ≈ 4 caracteres em inglês** ou **cerca de 1 sílaba**. Em português, por conta de palavras mais longas e acentuação, tende a ser um pouco menos eficiente.

**Exemplos concretos:**

| Texto | Aproximação em tokens |
|---|---|
| `"Olá"` | 1 token |
| `"programação"` | 3 tokens (pro-gra-ma-ção) |
| `"Inteligência Artificial"` | ~5 tokens |
| Um tweet de 280 caracteres | ~70 tokens |
| Uma página de livro (~400 palavras) | ~500–600 tokens |
| Este plano de aula inteiro | ~8.000–10.000 tokens |

**Por que isso importa?**

Porque **você paga por token**. Cada requisição que seu app faz para a API consome tokens — tanto o texto que você manda (input) quanto o texto que o modelo devolve (output). Se você construir um app que faz chamadas ineficientes, o custo pode explodir muito rápido.

> 💡 **Demonstração ao vivo:** Acesse [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) e cole textos diferentes. Mostre como palavras em português geralmente geram mais tokens que as equivalentes em inglês. Peça que os alunos calculem quantos tokens têm seus próprios nomes.

---

### 1.3 A janela de contexto

O LLM não tem memória permanente entre conversas. O que ele "sabe" sobre a conversa atual é tudo o que está na **janela de contexto** — o bloco de texto que você mandou na requisição atual.

Pense assim: cada vez que você faz uma chamada à API, você manda tudo — o histórico da conversa, as instruções do sistema, a pergunta atual — em uma única requisição. O modelo lê tudo, gera a resposta, e "esquece" na próxima chamada.

```
┌──────────────────────────────────────────────────┐
│                JANELA DE CONTEXTO                 │
│                                                   │
│  [Instruções do sistema]                          │
│  "Você é um tutor de Python para adolescentes..." │
│                                                   │
│  [Histórico da conversa]                          │
│  Usuário: "O que é uma lista?"                    │
│  IA: "Uma lista é uma coleção de itens..."        │
│  Usuário: "E como eu adiciono itens?"             │
│  IA: "Você usa o método .append()..."             │
│                                                   │
│  [Pergunta atual]                                 │
│  Usuário: "Pode dar um exemplo?"                  │
└──────────────────────────────────────────────────┘
                        ↓
              [Resposta do modelo]
```

O tamanho máximo dessa janela varia por modelo — hoje os melhores modelos suportam janelas de **1 milhão de tokens** (o equivalente a vários livros). Isso tem implicações diretas para custo: enviar contextos longos consome muitos tokens de input.

---

### 1.4 Chat vs. API: a diferença que muda tudo

| | Chat (interface) | API (backend) |
|---|---|---|
| **Quem usa** | Qualquer pessoa | Desenvolvedores |
| **Como acessa** | Navegador ou app | Código Python |
| **Custo** | Assinatura mensal (ou gratuito com limites) | Por token consumido |
| **Personalização** | Limitada | Total |
| **Integração** | Impossível | Com qualquer sistema |
| **Escala** | Manual | Automático |

Quando você usa o ChatGPT, está usando a *interface* que a OpenAI construiu para o consumidor final. Por baixo, existe a mesma API que disponibilizam para desenvolvedores — e que você vai aprender a usar hoje.

> 💡 **Para reflexão:** *"Toda vez que você conversa com um chatbot de suporte de alguma empresa, provavelmente tem código muito parecido com o que vamos escrever hoje rodando por baixo."*

---

### 🎯 Verificação de compreensão — 1.5

> Responda sem pesquisar (vamos discutir depois):
>
> 1. Se uma resposta do modelo tem 300 tokens de output, e o custo é $2,00 por 1 milhão de tokens de output, quanto custa essa única resposta?
> 2. Por que mandar o histórico inteiro de uma conversa a cada nova mensagem pode ficar caro?
> 3. Qual a diferença entre o ChatGPT que você usa no navegador e a API que vamos chamar com Python?

---

## BLOCO 2 — O Mercado de IA: Provedores, Modelos e Custos (1h)

### Objetivo
O aluno conhece os principais provedores, entende a hierarquia de modelos (flagship → mini → nano), e sabe por que escolher o modelo certo é a principal alavanca de custo.

---

### 2.1 Os grandes provedores

O mercado de LLMs converge em alguns grandes players, cada um com estratégias diferentes:

---

#### OpenAI — o pioneiro

A empresa criadora do ChatGPT, e ainda referência de fato do setor. Quando a maioria das pessoas fala "IA", ainda pensa no ChatGPT.

**Linha de modelos atual (maio/2026):**

| Modelo | Posicionamento | Input ($/1M tokens) | Output ($/1M tokens) |
|---|---|---|---|
| GPT-5.5 | Flagship máximo | $5,00 | $30,00 |
| GPT-5.4 | Flagship padrão | $2,50 | $15,00 |
| GPT-5.4 Mini | Custo-benefício | $0,75 | $4,50 |
| GPT-5.4 Nano | Ultra econômico | $0,20 | $1,25 |

> ⚠️ **Preços mudam constantemente.** Os valores acima são referência de maio/2026. Sempre confira [platform.openai.com/docs/pricing](https://platform.openai.com/docs/pricing) antes de lançar qualquer produto.

---

#### Google Gemini — o forte concorrente

O Google entrou na corrida da IA com força total. O Gemini tem uma vantagem enorme para quem está aprendendo: **o tier gratuito é genuinamente generoso**.

**Linha de modelos atual:**

| Modelo | Posicionamento | Gratuito? |
|---|---|---|
| Gemini 2.5 Pro | Alta capacidade de raciocínio | ✅ (limite: 50 req/dia) |
| Gemini 2.5 Flash | Equilíbrio velocidade/qualidade | ✅ (até ~1.500 req/dia) |
| Gemini 2.5 Flash-Lite | Máxima velocidade e volume | ✅ (até ~1.500 req/dia) |
| Gemini 3.x | Nova geração (em preview) | ❌ (somente pago) |

> 💡 **Por isso o Gemini é nossa escolha no curso:** você consegue construir e testar apps reais sem precisar de cartão de crédito. Para projetos de aprendizado e portfólio, o free tier do Gemini 2.5 Flash é mais do que suficiente.

---

#### Anthropic Claude — foco em segurança

A Anthropic foi fundada por ex-funcionários da OpenAI com foco em IA mais segura e confiável. O Claude é conhecido por seguir instruções com mais precisão e ter respostas mais longas e coerentes.

| Modelo | Input ($/1M tokens) | Output ($/1M tokens) |
|---|---|---|
| Claude Opus 4.6 | $5,00 | $25,00 |
| Claude Sonnet 4.6 | $3,00 | $15,00 |
| Claude Haiku 4.5 | $1,00 | $5,00 |

---

#### DeepSeek — a surpresa chinesa

Em janeiro de 2025, a empresa chinesa DeepSeek lançou modelos com performance comparável aos melhores modelos ocidentais a uma fração do custo. Isso gerou um impacto gigante no mercado — as ações da NVIDIA caíram bilhões de dólares em um único dia.

O DeepSeek V3 custa em torno de **$0,28 por milhão de tokens de input** — dezenas de vezes mais barato que o GPT-5.4. Ele é open-source, o que significa que qualquer empresa pode baixar e rodar na própria infraestrutura.

> 💡 **Para discussão:** *"Por que o lançamento do DeepSeek fez as ações da NVIDIA despencar? O que isso diz sobre as apostas que o mercado estava fazendo?"* — A hipótese dominante era que treinar e rodar modelos poderosos exigiria cada vez mais GPUs. O DeepSeek provou que dá para chegar em resultado similar com muito menos hardware.

---

#### Modelos Open-Source — a alternativa independente

Além dos provedores comerciais, existe um ecossistema robusto de modelos que podem ser baixados e rodados localmente, sem enviar dados para nenhum servidor externo:

- **Meta Llama** — linha de modelos da Meta, livre para uso comercial
- **Mistral** — empresa francesa com modelos compactos e eficientes
- **DeepSeek** (versão open-source) — o mesmo modelo mencionado acima, disponível para download

A ferramenta mais popular para rodar modelos localmente é o **Ollama** — com um comando você baixa e roda Llama, Mistral ou qualquer outro modelo na própria máquina. Custo: zero. Privacidade: total. Desvantagem: precisa de um computador razoável (quanto mais potente, melhor).

---

### 2.2 A lógica de preços — e como não quebrar o banco

Todo provedor usa a mesma estrutura:

```
Custo = (tokens de input × preço_input) + (tokens de output × preço_output)
```

**Exemplo prático:** app de análise de currículos

- System prompt: 200 tokens
- Currículo do usuário: 800 tokens
- Resposta do modelo: 400 tokens

Com GPT-5.4 ($2,50 input / $15,00 output por 1M tokens):
```
Input:  1.000 tokens × $2,50/1M  = $0,0025 por análise
Output:   400 tokens × $15,00/1M = $0,0060 por análise
Total:  ≈ $0,0085 por análise = menos de 1 centavo
```

Com 1.000 análises por mês: **$8,50/mês** — viável para uma startup.

Mas se o mesmo app usasse GPT-5.5 ($5/$30):
```
Total: ≈ $0,017 por análise → $17,00/mês com o mesmo tráfego
```

**Escolher o modelo certo é a maior alavanca de custo que você tem.** A regra prática:
- Use modelos menores (Mini, Flash) para tarefas simples: extração de dados, classificação, resumos curtos
- Reserve os modelos maiores para tarefas que realmente exigem raciocínio: análise complexa, código elaborado, argumentação

---

### 2.3 A hierarquia dos modelos — uma visualização

```
                    QUALIDADE / CUSTO
                          ↑
          ┌───────────────────────────────┐
          │  GPT-5.5 / Claude Opus 4.6   │  ← Tarefas muito complexas
          │  Gemini 2.5 Pro               │    Raciocínio avançado
          ├───────────────────────────────┤
          │  GPT-5.4 / Claude Sonnet 4.6 │  ← Uso geral
          │  Gemini 2.5 Flash             │    Apps de produção
          ├───────────────────────────────┤
          │  GPT-5.4 Mini / Haiku 4.5    │  ← Alta frequência
          │  Gemini 2.5 Flash-Lite        │    Extração, classificação
          ├───────────────────────────────┤
          │  GPT-5.4 Nano / DeepSeek     │  ← Máximo volume
          │  Modelos open-source          │    Tarefas simples
          └───────────────────────────────┘
                          ↓
                  VELOCIDADE / VOLUME
```

---

### 2.4 Demonstração — A plataforma da OpenAI

> *"Vamos entrar na plataforma da OpenAI porque é onde a maioria de vocês já teve o primeiro contato com IA. Quero mostrar o que existe por baixo da interface que vocês conhecem."*

Mostre ao vivo, navegando em [platform.openai.com](https://platform.openai.com):

1. **Playground** — interface para testar modelos diretamente, ver tokens sendo contados em tempo real
2. **API Keys** — onde se gera a chave de acesso programático
3. **Usage** — painel de consumo, onde se vê quanto foi gasto
4. **Pricing** — tabela de preços por modelo

> 💡 **Ponto pedagógico chave:** No playground, habilite o contador de tokens e mostre como aumentar o system prompt muda o contador imediatamente. Faça uma chamada simples e mostre a seção "usage" na resposta — `prompt_tokens`, `completion_tokens`, `total_tokens`. Isso torna concreto algo que antes era abstrato.

---

## BLOCO 3 — Primeira Chamada Manual à API (45min)

### Objetivo
O aluno entende o que acontece por baixo de qualquer SDK ao ver uma requisição HTTP crua para a API da OpenAI. Compreende que uma chamada de IA é simplesmente uma requisição POST com um JSON específico.

---

### 3.1 A API é só uma URL

Antes de qualquer biblioteca ou SDK, existe uma verdade simples: **chamar um LLM é fazer uma requisição HTTP POST**. Exatamente como o ViaCEP e a RestCountries que vimos antes — só que você manda um JSON mais elaborado e recebe outro JSON de volta.

Todo SDK (biblioteca) que existe para OpenAI, Gemini, Claude — por baixo dos panos, faz exatamente o que vamos fazer agora: montar um JSON e mandar para uma URL.

---

### 3.2 Anatomia de uma requisição

A API da OpenAI (e a maioria dos provedores seguem estrutura similar) espera:

**URL:**
```
POST https://api.openai.com/v1/chat/completions
```

**Headers (cabeçalhos):**
```
Content-Type: application/json
Authorization: Bearer SUA_CHAVE_AQUI
```

**Body (corpo) — o JSON:**
```json
{
  "model": "gpt-5.4-mini",
  "messages": [
    {
      "role": "system",
      "content": "Você é um assistente útil."
    },
    {
      "role": "user",
      "content": "O que é um token em LLMs?"
    }
  ]
}
```

**Resposta que vem de volta:**
```json
{
  "id": "chatcmpl-abc123",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Um token é a unidade básica de texto que um LLM processa..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 28,
    "completion_tokens": 95,
    "total_tokens": 123
  }
}
```

---

### 3.3 Faça você mesmo — chamada crua com `requests`

*Construa junto com os alunos, passo a passo. Use a chave da OpenAI configurada para aula.*

```python
import requests
import json

# ─────────────────────────────────────────────
# CHAMADA MANUAL À API DA OPENAI
# Sem nenhuma biblioteca específica — só requests
# ─────────────────────────────────────────────

OPENAI_API_KEY = "sk-..."   # ← chave do professor, só para demonstração

url = "https://api.openai.com/v1/chat/completions"

# Os headers identificam quem está fazendo a requisição
# e o formato do conteúdo enviado
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# O body é um dicionário Python que será convertido para JSON
body = {
    "model": "gpt-4.1-mini",      # modelo atual, confirme em platform.openai.com
    "messages": [
        {
            "role": "system",
            "content": "Você é um tutor de Python para adolescentes. Responda de forma clara e com exemplos simples."
        },
        {
            "role": "user",
            "content": "Explique o que é uma função em Python em 2 frases."
        }
    ]
}

# requests.post() manda o JSON e retorna a resposta
resposta = requests.post(url, headers=headers, json=body)

# Convertemos a resposta para dicionário Python — exatamente como sempre fizemos
dados = resposta.json()

# Imprimimos para ver a estrutura completa
print(json.dumps(dados, indent=2, ensure_ascii=False))
```

Rode. Mostre o JSON de resposta inteiro no terminal. Depois extraia só o que importa:

```python
# Extraindo a resposta da IA do dicionário
texto_resposta = dados["choices"][0]["message"]["content"]
print("\n=== RESPOSTA DA IA ===")
print(texto_resposta)

# Verificando o consumo de tokens
tokens_usados = dados["usage"]["total_tokens"]
print(f"\n=== TOKENS USADOS: {tokens_usados} ===")
```

> 💡 **Ponto pedagógico:** Pause aqui e pergunte: *"Olhando esse código, o que é diferente de qualquer outra chamada de API que já fizemos no curso?"* A resposta é: quase nada. A única diferença real é o header de autenticação e o formato específico do JSON. Todo o resto — `requests.post()`, `.json()`, acessar chaves do dicionário — é igual.

---

### 3.4 A mesma estrutura, provedores diferentes

Mostrar brevemente que a Anthropic (Claude) usa estrutura idêntica:

```python
# Claude — Anthropic API (estrutura quase idêntica)
url = "https://api.anthropic.com/v1/messages"

headers = {
    "Content-Type": "application/json",
    "x-api-key": "SUA_CHAVE_ANTHROPIC",
    "anthropic-version": "2023-06-01"    # ← única diferença: header de versão
}

body = {
    "model": "claude-haiku-4-5",
    "max_tokens": 1024,
    "messages": [
        {
            "role": "user",
            "content": "Explique o que é uma função em Python em 2 frases."
        }
    ]
}
```

> *"O padrão muda um pouco entre provedores — o nome dos campos, o header de autenticação — mas a ideia é sempre a mesma: POST + JSON com as mensagens + chave de autenticação. Quando vocês virem um SDK novo, saibam que por baixo é isso."*

---

## BLOCO 4 — SDKs: A Camada de Abstração (45min)

### Objetivo
O aluno entende o que é um SDK, por que ele existe, e como usar o SDK do Gemini — que será a ferramenta do curso.

---

### 4.1 O que é um SDK e por que usar

SDK significa **Software Development Kit** — um kit de ferramentas que um provedor disponibiliza para facilitar a integração.

Em vez de você escrever todo o código de requisição HTTP, montar os headers, tratar os erros de rede, e navegar no JSON de resposta... o SDK encapsula tudo isso em funções simples.

**Comparação lado a lado:**

```python
# ─── SEM SDK — 20 linhas para uma chamada simples ───────────────
import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
body = {
    "model": "gpt-5.4-mini",
    "messages": [{"role": "user", "content": pergunta}]
}
resposta = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=body
)
dados = resposta.json()
texto = dados["choices"][0]["message"]["content"]


# ─── COM SDK OpenAI — 5 linhas para o mesmo resultado ──────────
from openai import OpenAI

cliente = OpenAI(api_key=api_key)
resposta = cliente.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": pergunta}]
)
texto = resposta.choices[0].message.content
```

O resultado é idêntico. O SDK só esconde o trabalho repetitivo.

> 💡 **Por que entendemos o "sem SDK" primeiro?** Porque quando algo der errado — e vai dar — você vai precisar entender o que está acontecendo por baixo. Um erro de autenticação, um campo mal formatado, uma mudança na API... quem entende o protocolo HTTP consegue depurar. Quem só sabe usar o SDK fica perdido.

---

### 4.2 Cada provedor tem seu SDK

| Provedor | Pacote Python | Instalação |
|---|---|---|
| OpenAI | `openai` | `pip install openai` |
| Google Gemini | `google-genai` | `pip install google-genai` |
| Anthropic Claude | `anthropic` | `pip install anthropic` |

Todos seguem a mesma filosofia: criar um cliente, chamar um método com o modelo e as mensagens, receber a resposta.

---

### 4.3 O SDK do Gemini — que vamos usar no curso

O Google disponibiliza o pacote `google-genai`. A sintaxe é limpa e direta.

**Instalação:**
```bash
pip install google-genai
```

**Uso básico:**
```python
from google import genai
from google.genai import types

# Cria o cliente — a chave pode vir de uma variável ou diretamente
cliente = genai.Client(api_key="SUA_CHAVE_AQUI")

# Faz a chamada
resposta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explique o que é uma função em Python em 2 frases."
)

# Acessa o texto da resposta
print(resposta.text)
```

**Com system prompt (instrução de sistema):**
```python
resposta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explique o que é uma função em Python em 2 frases.",
    config=types.GenerateContentConfig(
        # system_instruction define o comportamento geral do modelo.
        system_instruction="Você é um tutor de Python para adolescentes brasileiros. Use linguagem simples e exemplos do cotidiano."
    )
)
print(resposta.text)
```

**Verificando o consumo de tokens:**
```python
if resposta.usage_metadata:
    # Esses campos mostram quanto foi gasto na chamada.
    print(f"Tokens de input:  {resposta.usage_metadata.prompt_token_count}")
    print(f"Tokens de output: {resposta.usage_metadata.candidates_token_count}")
    print(f"Total:            {resposta.usage_metadata.total_token_count}")
```

> 💡 **Por que `gemini-2.5-flash` e não o Pro?** O Flash tem free tier generoso (~1.500 requisições por dia, sem cartão de crédito) e qualidade mais que suficiente para os projetos do curso. O Pro tem limite de apenas 50 requisições por dia no free tier — o suficiente para testar, não para desenvolver. **Quando o modelo evoluir, verifique o modelo recomendado atual em [ai.google.dev](https://ai.google.dev).**

---

### 4.4 Onde obter a chave da API do Gemini

1. Acesse [aistudio.google.com](https://aistudio.google.com)
2. Faça login com uma conta Google
3. Clique em **"Get API key"** no menu lateral
4. Clique em **"Create API key"**
5. Copie a chave gerada (começa com `AIza...`)

> ⚠️ **Regras de segurança para chaves de API:**
> - Nunca coloque a chave diretamente em código que vai para o GitHub
> - Para projetos locais em desenvolvimento: pode colocar direto no código, mas com cuidado
> - Para Streamlit: use `st.secrets` (veremos no próximo bloco)
> - Para produção: use variáveis de ambiente

---

## BLOCO 5 — Gemini no Curso: Configuração e Primeiros Experimentos (1h30)

### Objetivo
O aluno configura sua própria chave do Gemini, faz sua primeira chamada bem-sucedida, e entende como o `system_instruction` muda o comportamento do modelo.

---

### 5.1 Padrão de função para chamadas ao Gemini

Assim como usamos o padrão `(dados, erro)` para APIs REST no curso, vamos adotar um padrão consistente para chamadas ao Gemini:

```python
from google import genai
from google.genai import types

GEMINI_API_KEY = "AIza..."   # ← substituir pela chave real
MODEL = "gemini-2.5-flash"

cliente = genai.Client(api_key=GEMINI_API_KEY)


def chamar_gemini(mensagem, instrucao_sistema=None):
    """
    Faz uma chamada ao Gemini e retorna (resposta, erro).
    
    - mensagem: string com o que você quer perguntar
    - instrucao_sistema: string com instruções de comportamento (opcional)
    
    Retorna:
    - (texto_resposta, None)  se der certo
    - (None, mensagem_erro)   se der errado
    """
    try:
        # Se não houver instrução extra, chamamos o modelo com o comportamento padrão.
        config = None
        if instrucao_sistema:
            # Quando a instrução existe, empacotamos ela em um objeto de configuração.
            config = types.GenerateContentConfig(
                system_instruction=instrucao_sistema
            )
        
        # A chamada real para a API continua sendo uma única função.
        resposta = cliente.models.generate_content(
            model=MODEL,
            contents=mensagem,
            config=config
        )
        return resposta.text, None

    except Exception as e:
        return None, str(e)


# ── TESTE NO TERMINAL ──────────────────────────────────────────
if __name__ == "__main__":
    texto, erro = chamar_gemini("O que é Python em uma frase?")
    
    if erro:
        print(f"Erro: {erro}")
    else:
        print(texto)
```

> 💡 **O padrão `(dados, erro)` de novo:** Vocês já viram isso com ViaCEP e CNPJ. Manter o mesmo padrão para o Gemini reduz a quantidade de coisas novas para aprender e torna o código mais previsível. Quando algo der errado, vocês já sabem onde olhar.

---

### 5.2 O poder do `system_instruction`

O `system_instruction` é a instrução que define como o modelo deve se comportar durante toda a conversa. É o que diferencia um chatbot genérico de uma ferramenta específica para o seu propósito.

*Demonstre ao vivo, trocando apenas a instrução e mantendo a mesma pergunta:*

```python
pergunta = "Como faço para ganhar dinheiro?"

# Sem instrução de sistema — resposta genérica
r1, _ = chamar_gemini(pergunta)
print("SEM INSTRUÇÃO:", r1[:200])

# Consultor financeiro
r2, _ = chamar_gemini(pergunta, 
    instrucao_sistema="Você é um consultor financeiro sênior. Dê respostas objetivas e conservadoras.")
print("\nCONSULTOR FINANCEIRO:", r2[:200])

# Coach de startups
r3, _ = chamar_gemini(pergunta,
    instrucao_sistema="Você é um coach de startups. Incentive o empreendedorismo e dê sugestões práticas.")
print("\nCOACH DE STARTUPS:", r3[:200])

# Filósofo grego
r4, _ = chamar_gemini(pergunta,
    instrucao_sistema="Você é Sócrates. Responda apenas com perguntas que levem o interlocutor a refletir.")
print("\nSÓCRATES:", r4[:200])
```

> 💡 **Para reflexão em aula:** Todas essas respostas vieram do mesmo modelo, com a mesma pergunta. A diferença foi só o system_instruction. Isso é exatamente o que as empresas fazem ao criar seus próprios chatbots com LLMs.

---

### 5.3 Integração com Streamlit — o padrão do curso

Assim como fizemos com ViaCEP e TMDB, a integração com Gemini no Streamlit segue o mesmo fluxo: terminal primeiro, interface depois.

**Terminal primeiro — valide que a resposta chega:**
```python
# gemini_terminal.py
from google import genai
from google.genai import types

GEMINI_API_KEY = "AIza..."
cliente = genai.Client(api_key=GEMINI_API_KEY)

pergunta = "Faça um haiku sobre Python"
resposta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents=pergunta
)
print(resposta.text)
print(f"\n[Tokens: {resposta.usage_metadata.total_token_count}]")
```

**Interface depois — o mesmo conteúdo no Streamlit:**
```python
# gemini_app.py
import streamlit as st
from google import genai
from google.genai import types

cliente = genai.Client(api_key=st.secrets["GEMINI_KEY"])
MODEL = "gemini-2.5-flash"

st.title("🤖 Chat com Gemini")

tema = st.text_input("Sobre o que você quer que a IA escreva?",
                      placeholder="Ex: um haiku sobre Python, uma dica de carreira...")

if st.button("Gerar"):
    if not tema:
        st.error("Digite algo primeiro!")
    else:
        with st.spinner("Gerando..."):
            resposta = cliente.models.generate_content(
                model=MODEL,
                contents=tema
            )
        
        st.markdown(resposta.text)
        st.caption(f"Tokens usados: {resposta.usage_metadata.total_token_count}")
```

> 💡 **`st.secrets` com Gemini:** Crie o arquivo `.streamlit/secrets.toml` na pasta do projeto com:
> ```toml
> GEMINI_KEY = "AIza..."
> ```
> No código, acesse com `st.secrets["GEMINI_KEY"]`. No Streamlit Cloud, configure pelo painel web.

---

### 🎯 Mini-Desafio 5A — Primeiro App com IA *(~20 min)*

> Crie um app Streamlit com:
> - Um `st.text_input` onde o usuário escolhe um "papel" para a IA (ex: "chef de cozinha", "professor de história", "narrador esportivo")
> - Um `st.text_area` para a pergunta
> - Um botão "Perguntar"
> - A resposta exibida com `st.markdown()`
> - O número de tokens exibido com `st.caption()`
>
> ✅ Critério: a resposta muda conforme o papel escolhido para a IA.

---

### 🎯 Mini-Desafio 5B — Contador de Custos *(~25 min)*

> Expanda o app anterior adicionando:
> - Um `st.session_state` que acumula o total de tokens usados durante a sessão
> - Um `st.metric()` no sidebar mostrando "Tokens desta sessão"
> - Um cálculo estimado do custo (use $0,30 por 1M tokens de input e $2,50 por 1M de output como referência do Gemini 2.5 Flash pago)
> - Um botão "Zerar contador" que reseta o `session_state`
>
> ✅ Critério: o contador aumenta a cada chamada e exibe um valor estimado de custo.

---

### 🎯 Desafio 5C — FoodGrader Turbo *(~45 min)*

> Revise o FoodGrader construído no módulo de Streamlit para usar o Gemini no lugar da API da Anthropic.
>
> **Mudanças necessárias:**
> - Substituir o cliente Anthropic pelo cliente Gemini
> - Adaptar o envio de imagem (o Gemini aceita imagem diretamente via `types.Part.from_bytes()`)
> - Manter o mesmo sistema de exibição de resultado
>
> **Envio de imagem com Gemini:**
> ```python
> from google.genai import types
>
> imagem_bytes = imagem.getvalue()
> parte_imagem = types.Part.from_bytes(
>     data=imagem_bytes,
>     mime_type="image/jpeg"
> )
>
> resposta = cliente.models.generate_content(
>     model="gemini-2.5-flash",
>     contents=[parte_imagem, "Analise essa comida e retorne NOTA, CALORIAS, AVALIACAO..."]
> )
> ```
>
> ✅ Critério: app funciona com câmera ou upload, exibe nota e avaliação, roda no free tier do Gemini.

---

## Referência Rápida — Provedores e Modelos (maio/2026)

> ⚠️ **Este mercado muda rapidamente.** Modelos são lançados, renomeados e descontinuados com frequência. Sempre confira as páginas oficiais antes de usar em produção.

| Provedor | Modelo econômico | Free tier? | Onde criar a chave |
|---|---|---|---|
| Google Gemini | `gemini-2.5-flash` | ✅ ~1.500 req/dia | aistudio.google.com |
| OpenAI | `gpt-5.4-mini` | ❌ (créditos iniciais) | platform.openai.com |
| Anthropic | `claude-haiku-4-5` | ❌ (créditos iniciais) | console.anthropic.com |
| DeepSeek | `deepseek-chat` | Créditos iniciais | platform.deepseek.com |

---

## Referência Rápida — SDK do Gemini

```python
# ── INSTALAÇÃO ──────────────────────────────────────────────────
# pip install google-genai

# ── IMPORTS E CONFIGURAÇÃO ──────────────────────────────────────
from google import genai
from google.genai import types

cliente = genai.Client(api_key="SUA_CHAVE")
MODEL = "gemini-2.5-flash"

# ── CHAMADA SIMPLES ─────────────────────────────────────────────
resposta = cliente.models.generate_content(
    model=MODEL,
    contents="Sua pergunta aqui"
)
print(resposta.text)

# ── COM INSTRUÇÃO DE SISTEMA ────────────────────────────────────
resposta = cliente.models.generate_content(
    model=MODEL,
    contents="Sua pergunta aqui",
    config=types.GenerateContentConfig(
        system_instruction="Você é um especialista em..."
    )
)
print(resposta.text)

# ── COM IMAGEM ──────────────────────────────────────────────────
parte_imagem = types.Part.from_bytes(
    data=bytes_da_imagem,
    mime_type="image/jpeg"
)
resposta = cliente.models.generate_content(
    model=MODEL,
    contents=[parte_imagem, "Descreva esta imagem"]
)
print(resposta.text)

# ── VERIFICAR TOKENS ────────────────────────────────────────────
if resposta.usage_metadata:
    print(resposta.usage_metadata.total_token_count)

# ── PADRÃO (dados, erro) ─────────────────────────────────────────
def chamar_gemini(mensagem, instrucao=None):
    try:
        config = types.GenerateContentConfig(
            system_instruction=instrucao
        ) if instrucao else None
        r = cliente.models.generate_content(
            model=MODEL, contents=mensagem, config=config
        )
        return r.text, None
    except Exception as e:
        return None, str(e)
```

---

## Glossário — Termos Essenciais de IA

| Termo | Significado |
|---|---|
| **LLM** | Large Language Model — Modelo de Linguagem Grande |
| **Token** | Unidade de texto que o modelo processa (~4 chars em inglês) |
| **Context window** | Quantidade máxima de tokens que o modelo processa por vez |
| **Input tokens** | Tokens enviados para o modelo (seu prompt) |
| **Output tokens** | Tokens gerados pelo modelo (a resposta) |
| **System prompt / instruction** | Instrução que define o comportamento do modelo |
| **Temperature** | Controle de criatividade (0 = determinístico, 1 = criativo) |
| **API Key** | Chave de acesso programático ao serviço |
| **SDK** | Software Development Kit — biblioteca que simplifica o uso da API |
| **Inference** | O ato de "rodar" o modelo para gerar uma resposta |
| **Open-source** | Modelos cujo código/pesos são públicos e podem ser rodados localmente |

---

*Plano elaborado para turmas do ensino médio público — foco em fundamentos sólidos antes da prática guiada.*
*Próxima expansão: prática guiada com projetos progressivos usando Gemini + Streamlit.*
