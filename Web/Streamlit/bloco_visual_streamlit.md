# 🎨 Visual e Identidade — Personalize o Visual do Seu App

**Módulo complementar | Curso Python + APIs**

| Duração | Público | Pré-requisito |
|---|---|---|
| ~45min | Ensino médio público, adolescentes | App Streamlit funcionando localmente |

---

## A conversa honesta antes de começar

Todo app Streamlit começa igual: fundo branco, texto cinza escuro, botões vermelho-laranja. Isso não é ruim — é limpo e funcional. Mas quando você quer mostrar o app para alguém, a primeira coisa que as pessoas percebem é a aparência.

Dois apps com o mesmo código — um com o visual padrão, outro com uma paleta de cores própria, uma fonte diferente e um logo no topo — causam impressões completamente diferentes. O segundo parece produto. O primeiro parece exercício escolar.

Esse guia mostra como ir de um para o outro em menos de 30 minutos, sem precisar aprender CSS do zero.

---

## O que dá pra customizar

| O que | Onde configurar | Dificuldade |
|---|---|---|
| Título e ícone da aba do navegador | `st.set_page_config()` | ⭐ |
| Layout (centralizado ou largura total) | `st.set_page_config()` | ⭐ |
| Cores (fundo, botões, texto) | `.streamlit/config.toml` | ⭐⭐ |
| Fonte do texto | `.streamlit/config.toml` | ⭐⭐ |
| Borda dos widgets | `.streamlit/config.toml` | ⭐⭐ |
| Logo na sidebar | `st.logo()` | ⭐ |
| Cabeçalho com imagem | `st.image()` | ⭐ |
| CSS customizado avançado | `st.markdown()` | ⭐⭐⭐ |

---

## PARTE 1 — Vitórias rápidas com `st.set_page_config()`

Essa função configura a "casca" do app — o que aparece na aba do navegador e como a página se organiza. Ela precisa ser a **primeira linha de código** depois do `import streamlit as st`, antes de qualquer outro widget.

```python
import streamlit as st

st.set_page_config(
    page_title="Buscador de Filmes",   # aparece na aba do navegador
    page_icon="🎬",                     # emoji ou caminho para imagem .png/.ico
    layout="centered",                  # "centered" (padrão) ou "wide"
    initial_sidebar_state="expanded",   # "auto", "expanded" ou "collapsed"
)

st.title("Meu App")
```

### `layout="wide"` vs `layout="centered"`

| `centered` (padrão) | `wide` |
|---|---|
| Conteúdo centralizado com margens | Ocupa toda a largura da tela |
| Melhor para apps de consulta simples | Melhor para dashboards e tabelas |
| Parece mais um site | Parece mais um painel de dados |

> 💡 Para o app do TMDB, `layout="centered"` costuma ficar mais elegante. Para um app com várias colunas e gráficos lado a lado, experimente `layout="wide"`.

---

## PARTE 2 — O arquivo de tema: `config.toml`

Esse arquivo é onde você define as cores, fontes e formato dos cantos de todo o app. Ele fica dentro da pasta `.streamlit/` — a mesma onde está o `secrets.toml`.

### Estrutura das pastas

```
meu_app/
├── app_tmdb.py
├── requirements.txt
├── .gitignore
└── .streamlit/
    ├── secrets.toml    ← chaves de API (não vai pro GitHub)
    └── config.toml     ← visual do app (vai pro GitHub ✅)
```

> ✅ Diferente do `secrets.toml`, o `config.toml` **deve** ir para o GitHub — é ele que faz o app publicado no Streamlit Cloud ter o mesmo visual que o local.

---

### 2.1 Criando o `config.toml`

Crie o arquivo `.streamlit/config.toml` com o seguinte conteúdo mínimo:

```toml
[theme]
base = "dark"
primaryColor = "#F5C518"
backgroundColor = "#0F0F0F"
secondaryBackgroundColor = "#1C1C1C"
textColor = "#FFFFFF"
font = "sans serif"
```

Salve e o app vai atualizar automaticamente.

---

### 2.2 O que cada opção faz

| Opção | O que controla | Exemplo |
|---|---|---|
| `base` | Tema base herdado | `"light"` ou `"dark"` |
| `primaryColor` | Cor dos botões, sliders e links | `"#F5C518"` |
| `backgroundColor` | Cor de fundo da página | `"#0F0F0F"` |
| `secondaryBackgroundColor` | Cor dos widgets e sidebar | `"#1C1C1C"` |
| `textColor` | Cor do texto principal | `"#FFFFFF"` |
| `font` | Família de fonte | `"sans serif"`, `"serif"`, `"monospace"` |
| `baseRadius` | Arredondamento dos cantos | `"none"`, `"small"`, `"medium"`, `"large"`, `"full"` |

> 💡 Todas as cores usam o formato **hexadecimal** (`#RRGGBB`). Se você não souber o código de uma cor, use **coolors.co** ou qualquer seletor de cor do Google digitando "color picker" na busca.

---

### 2.3 Iteração ao vivo — veja as mudanças na hora

A forma mais rápida de encontrar o tema certo é editar o `config.toml` e ver o resultado em tempo real:

1. Com o app rodando no navegador, vá no menu (**⋮** no canto superior direito)
2. Clique em **Settings**
3. Ative a opção **"Run on save"**

A partir daí, toda vez que você salvar o `config.toml`, o app atualiza sozinho. Você pode ajustar as cores e ver o resultado imediatamente, sem precisar recarregar nada.

---

### 2.4 Exemplo: tema inspirado no TMDB

O site oficial do TMDB usa azul escuro e verde-água. Aqui está um tema que copia essa identidade visual:

```toml
[theme]
base = "dark"
primaryColor = "#01B4E4"
backgroundColor = "#032541"
secondaryBackgroundColor = "#0D253F"
textColor = "#FFFFFF"
font = "sans serif"
baseRadius = "medium"
```

E um tema mais sóbrio, estilo cinema clássico:

```toml
[theme]
base = "dark"
primaryColor = "#F5C518"
backgroundColor = "#1A1A1A"
secondaryBackgroundColor = "#242424"
textColor = "#F0F0F0"
font = "serif"
baseRadius = "small"
```

> 💡 `#F5C518` é o amarelo do IMDb. Usar a cor de uma marca conhecida no tema passa credibilidade visual imediata.

---

## PARTE 3 — Logo e cabeçalho

### 3.1 Logo na sidebar com `st.logo()`

O `st.logo()` adiciona uma imagem fixada no topo da sidebar. Funciona com arquivo local ou URL.

```python
import streamlit as st

# Com arquivo local (coloque a imagem na pasta do projeto)
st.logo("logo.png")

# Com URL da internet
st.logo("https://exemplo.com/logo.png")

# Com tamanho controlado por link (apenas URL)
st.logo("logo.png", size="large")  # "small", "medium" ou "large"
```

> 💡 Para criar um logo simples e gratuito: **canva.com** tem templates prontos, exporte como PNG com fundo transparente. Funciona muito bem como logo de sidebar.

---

### 3.2 Cabeçalho com imagem usando `st.image()`

Para um banner no topo do app (não na sidebar), use `st.image()` antes do título:

```python
import streamlit as st

# Banner no topo, largura total
st.image("banner.png", use_container_width=True)
st.title("🎬 Buscador de Filmes")
```

Ou uma versão mais compacta com o logo ao lado do título usando colunas:

```python
import streamlit as st

col_logo, col_titulo = st.columns([1, 5])

with col_logo:
    st.image("logo.png", width=80)

with col_titulo:
    st.title("Buscador de Filmes")
    st.caption("Powered by TMDB API")
```

---

### 3.3 Favicon personalizado (ícone da aba)

Para usar uma imagem como ícone da aba do navegador em vez de um emoji:

```python
from PIL import Image

favicon = Image.open("favicon.png")

st.set_page_config(
    page_title="Meu App",
    page_icon=favicon,   # imagem PIL em vez de emoji
)
```

> 💡 O favicon precisa ser quadrado para ficar bem. Dimensões ideais: 32x32 ou 64x64 pixels.

---

## PARTE 4 — CSS customizado *(avançado, opcional)*

Se o `config.toml` não for suficiente para o que você quer fazer, dá para injetar CSS diretamente no app. Isso é avançado — use com moderação, porque um CSS mal feito pode quebrar o layout do Streamlit.

### O padrão básico

```python
import streamlit as st

st.markdown("""
    <style>
    /* Muda a fonte do título principal */
    h1 {
        font-family: 'Georgia', serif;
        color: #F5C518;
    }

    /* Muda a cor de fundo de todo o app */
    .stApp {
        background-color: #1A1A1A;
    }

    /* Aumenta o padding interno dos botões */
    .stButton > button {
        padding: 0.6rem 2rem;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)
```

> ⚠️ `unsafe_allow_html=True` é obrigatório para injetar HTML/CSS no Streamlit. O nome "unsafe" existe porque HTML mal formado pode quebrar o app — use apenas CSS dentro do `<style>`, nunca HTML com scripts.

### Quando usar CSS e quando usar o `config.toml`

| Situação | Use |
|---|---|
| Mudar cor dos botões, fundo, texto | `config.toml` — mais simples e seguro |
| Mudar fonte de títulos especificamente | CSS |
| Ajustar espaçamento ou padding | CSS |
| Esconder o menu do Streamlit | CSS |
| Qualquer coisa que o `config.toml` não cobre | CSS |

---

## PARTE 5 — Recursos e inspiração

### 5.1 Para criar paletas de cores

| Site | Para que serve |
|---|---|
| **coolors.co** | Gerador de paletas harmônicas — aperte a barra de espaço para gerar |
| **colorhunt.co** | Paletas prontas com votação da comunidade — ótimo para inspiração rápida |
| **google.com → "color picker"** | Seletor de cores direto no Google — pega o hex na hora |
| **contrast-ratio.com** | Verifica se texto e fundo têm contraste suficiente para leitura |

---

### 5.2 Temas prontos para copiar

**Awesome Streamlit Themes** — `github.com/jmedia65/awesome-streamlit-themes`

10 temas profissionais prontos para usar: healthcare, finance, dark pro, light minimal, e outros. Cada um tem o `config.toml` completo. Você baixa, cola na pasta `.streamlit/` e pronto.

**Dracula Theme** — `draculatheme.com/streamlit`

O clássico tema Dracula (roxo escuro e verde neon) portado para o Streamlit. Muito popular entre devs.

```toml
# Dracula — copie e cole direto no seu config.toml
[theme]
base = "dark"
primaryColor = "#BD93F9"
backgroundColor = "#282A36"
secondaryBackgroundColor = "#44475A"
textColor = "#F8F8F2"
```

**St_yled Studio** — comunidade Streamlit

Uma ferramenta interativa online onde você mexe nos controles deslizantes e vê o tema mudando ao vivo, depois exporta o `config.toml` gerado. Procure por "st_yled studio" no fórum do Streamlit (`discuss.streamlit.io`).

---

### 5.3 Para criar logo e banner

| Ferramenta | Para que serve |
|---|---|
| **canva.com** | Logo, banner e favicon — tem templates de app gratuitos |
| **favicon.io** | Gerador de favicon a partir de texto, emoji ou imagem |
| **shields.io** | Badges estilizados para o README do GitHub |

---

## Referência rápida

### `config.toml` mínimo funcional

```toml
[theme]
base = "dark"
primaryColor = "#sua-cor-aqui"
backgroundColor = "#sua-cor-aqui"
secondaryBackgroundColor = "#sua-cor-aqui"
textColor = "#sua-cor-aqui"
font = "sans serif"
```

### `set_page_config()` completo

```python
st.set_page_config(
    page_title="Nome do App",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded",
)
```

### Checklist de identidade visual

- [ ] `st.set_page_config()` está na primeira linha, com título e ícone definidos
- [ ] O arquivo `.streamlit/config.toml` existe e tem cores personalizadas
- [ ] O `config.toml` **não** está no `.gitignore` (ele deve ir para o GitHub)
- [ ] O contraste entre `textColor` e `backgroundColor` é legível
- [ ] O app foi testado em modo claro e escuro do sistema operacional

---

## Exemplo completo — app TMDB com identidade visual

```python
import streamlit as st
import requests

# ── IDENTIDADE VISUAL ───────────────────────
# (o config.toml cuida das cores — aqui só configuramos a aba)
st.set_page_config(
    page_title="CineSearch",
    page_icon="🎬",
    layout="centered",
)

# ── CABEÇALHO ───────────────────────────────
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    st.image("logo.png", width=70)          # substitua pelo seu logo
with col_titulo:
    st.title("CineSearch")
    st.caption("Busca de filmes • Powered by TMDB")

st.divider()

# ... restante do app normalmente
```

```toml
# .streamlit/config.toml — tema TMDB
[theme]
base = "dark"
primaryColor = "#01B4E4"
backgroundColor = "#032541"
secondaryBackgroundColor = "#0D253F"
textColor = "#FFFFFF"
font = "sans serif"
baseRadius = "medium"
```

---

*Guia elaborado para turmas do ensino médio público — foco em personalizar o app TMDB antes de publicar no portfólio.*
