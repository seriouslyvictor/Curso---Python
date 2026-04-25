# 🚀 Git, GitHub e Deploy — Leve seu App para a Internet

**Módulo complementar | Curso Python + APIs**

| Duração | Público | Pré-requisito |
|---|---|---|
| ~1h | Ensino médio público, adolescentes | App TMDB funcionando localmente |

---

## A conversa honesta antes de começar

Vocês fizeram o app do TMDB. Ele funciona na máquina de vocês. Mas se você tentar mandar o link pro seu melhor amigo, ele não vai conseguir acessar nada — porque esse app só existe no *seu* computador.

Para colocar um app na internet, precisamos de dois serviços. E os dois são gratuitos:

- **GitHub** — um serviço que guarda o seu código na nuvem. Pense como um Google Drive, mas só para código. Todo desenvolvedor profissional usa.
- **Streamlit Cloud** — um serviço que pega o código do GitHub, executa ele num servidor lá na nuvem, e te dá uma URL pública. Qualquer pessoa com o link consegue usar seu app.

O que conecta os dois é o **Git** — uma ferramenta que roda no terminal e "empurra" o código do seu computador para o GitHub.

> 💡 **Por que isso importa pra sua carreira?**
> Em qualquer estágio de TI, administração ou dados, saber usar Git é considerado conhecimento básico — como saber usar Excel em outras áreas. Não é avançado, é o mínimo. Você já vai sair daqui sabendo.

---

## PARTE 1 — Instalação e configuração inicial

### 1.1 Instalar o Git

**Windows:**
Acesse **git-scm.com**, baixe o instalador e execute. Nas opções, deixe tudo no padrão.

Depois de instalar, abra o **Git Bash** (aparece no menu iniciar) e confirme:
```bash
git --version
```
Deve aparecer algo como `git version 2.x.x`.

**Mac:**
```bash
git --version
```
Se não tiver, o Mac vai perguntar se quer instalar. Aceite.

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

---

### 1.2 Apresentar-se para o Git *(só uma vez por máquina)*

O Git precisa saber quem está fazendo as alterações. Use o mesmo e-mail que vai usar no GitHub:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

---

### 1.3 Criar conta no GitHub

Acesse **github.com** e crie uma conta gratuita.

> 💡 Use um e-mail que vai durar — esse perfil do GitHub vai ser seu portfólio profissional. Escolha um username sem números aleatórios: `joaosilva` é melhor que `joaosilva8823`.

---

## PARTE 2 — A regra de ouro antes de qualquer coisa

> 🔴 **NUNCA, JAMAIS, suba o arquivo `secrets.toml` para o GitHub.**

O `secrets.toml` contém sua chave da API do TMDB (e futuramente outras chaves). Se esse arquivo for para o GitHub — mesmo que o repositório seja privado — bots varrem o GitHub 24h por dia procurando exatamente isso. Sua chave pode ser roubada em minutos.

A proteção é simples: um arquivo chamado `.gitignore`.

### 2.1 Criar o `.gitignore`

Na pasta raiz do seu projeto, crie um arquivo chamado `.gitignore` (com ponto no começo, sem extensão):

```
# .gitignore

# Chaves de API — NUNCA subir isso
.streamlit/secrets.toml

# Arquivos temporários do Python
__pycache__/
*.pyc
.env
```

A partir de agora, o Git vai **ignorar completamente** qualquer arquivo listado aqui. Você pode dar `git add .` à vontade — o `secrets.toml` não vai junto.

---

## PARTE 3 — Estrutura final do projeto

Antes de subir qualquer coisa, seu projeto precisa estar organizado assim:

```
meu_app_tmdb/
│
├── app_tmdb.py              ← código principal do app
├── requirements.txt         ← lista de bibliotecas
├── .gitignore               ← lista do que NÃO subir
│
└── .streamlit/
    └── secrets.toml         ← chave da API (FICA SÓ LOCAL)
```

### 3.1 O arquivo `requirements.txt`

O Streamlit Cloud precisa saber quais bibliotecas instalar. Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```
streamlit
requests
```

> ⚠️ Não coloque versões específicas agora — o Streamlit Cloud vai pegar as versões mais recentes e compatíveis automaticamente.

---

## PARTE 4 — Os 4 comandos que você vai usar sempre

O Git tem dezenas de comandos, mas para o nosso uso, você precisa de exatamente 4. Aprenda esses e você já está no nível de qualquer dev júnior.

### O fluxo completo:

```
Seu computador                     GitHub
─────────────────────────────────────────
[arquivos editados]
       │
  git add .          ← "separa" o que vai ser salvo
       │
  git commit -m ""   ← "tira uma foto" do código com uma mensagem
       │
  git push           ← "envia a foto" para o GitHub
       │
                            [código atualizado na nuvem]
```

### Os comandos na prática:

| Comando | O que faz | Analogia |
|---|---|---|
| `git add .` | Marca todos os arquivos modificados para salvar | Escolher o que vai na mala |
| `git commit -m "mensagem"` | Salva um "ponto de restauração" com descrição | Tirar uma foto do estado atual |
| `git push` | Envia as alterações para o GitHub | Mandar a mala pelos Correios |
| `git status` | Mostra o que mudou e o que ainda não foi salvo | Ver o que ainda falta fazer |

---

## PARTE 5 — Do zero até o GitHub: passo a passo

### 5.1 Criar o repositório no GitHub

1. Entre no **github.com** com sua conta
2. Clique em **"New"** (botão verde no canto superior esquerdo)
3. Dê um nome ao repositório: `app-tmdb` ou `buscador-filmes`
4. Deixe como **Public** (necessário para o Streamlit Cloud gratuito)
5. **NÃO marque** nenhuma das opções extras (README, .gitignore, license)
6. Clique em **"Create repository"**

O GitHub vai mostrar uma tela com instruções. Copie a URL do repositório — vai parecer com:
```
https://github.com/seu-usuario/app-tmdb.git
```

---

### 5.2 Inicializar o Git na pasta do projeto

Abra o terminal **dentro da pasta do projeto** e rode os comandos um por vez:

```bash
# 1. Inicializa o Git nessa pasta (só uma vez por projeto)
git init

# 2. Conecta essa pasta ao repositório que você criou no GitHub
git remote add origin https://github.com/seu-usuario/app-tmdb.git

# 3. Confere o que vai ser enviado (boa prática sempre)
git status
```

O `git status` vai mostrar todos os arquivos em vermelho — isso significa que ainda não foram adicionados.

---

### 5.3 Primeiro envio

```bash
# 4. Adiciona todos os arquivos (exceto os do .gitignore)
git add .

# 5. Confere de novo — agora devem aparecer em verde
git status

# 6. Salva um "ponto de restauração" com uma mensagem descritiva
git commit -m "primeiro commit - app tmdb funcionando"

# 7. Envia para o GitHub
git push -u origin main
```

> 💡 Na primeira vez, o terminal pode pedir login. Use o usuário e senha do GitHub, ou configure um token de acesso pessoal (o GitHub vai orientar se necessário).

Acesse seu repositório no GitHub. O código vai estar lá. 🎉

---

### 5.4 Como atualizar depois de fazer mudanças

A partir de agora, sempre que modificar o app, o fluxo é esse — só 3 comandos:

```bash
git add .
git commit -m "descreva o que você mudou"
git push
```

Quando fizer o `push`, o Streamlit Cloud vai detectar automaticamente e publicar a versão nova em poucos segundos.

---

## PARTE 6 — Deploy no Streamlit Cloud

### 6.1 Conectar o Streamlit Cloud ao GitHub

1. Acesse **share.streamlit.io**
2. Clique em **"Sign in with GitHub"** e autorize
3. Clique em **"New app"**
4. Em **Repository**, escolha o repositório `app-tmdb`
5. Em **Branch**, deixe `main`
6. Em **Main file path**, coloque `app_tmdb.py` (o nome do seu arquivo principal)
7. **Não clique em Deploy ainda** — primeiro precisamos configurar as secrets

---

### 6.2 Configurar as secrets no Streamlit Cloud

Lembra que o `secrets.toml` ficou só no computador de vocês? Precisamos informar a chave para o Streamlit Cloud de outra forma.

Ainda na tela de configuração do app:

1. Clique em **"Advanced settings"**
2. No campo **Secrets**, cole o conteúdo do seu `secrets.toml`:

```toml
TMDB_TOKEN = "seu_bearer_token_aqui"
```

3. Agora sim, clique em **"Deploy!"**

O Streamlit Cloud vai instalar as bibliotecas do `requirements.txt` e iniciar o app. Demora em torno de 1-2 minutos na primeira vez.

---

### 6.3 Sua URL pública

Quando terminar, você vai ter uma URL no formato:

```
https://seu-usuario-app-tmdb-app-tmdb-xxxx.streamlit.app
```

Essa URL é pública. Qualquer pessoa com o link consegue usar seu app — sem instalar Python, sem instalar nada.

Manda pro grupo da família. Coloca no LinkedIn. Adiciona no currículo. É isso. 🚀

---

## PARTE 7 — Fluxo completo do dia a dia

Depois que tudo estiver configurado, a rotina de atualizar o app é essa:

```bash
# 1. Faz as mudanças no código
# 2. Testa localmente com: streamlit run app_tmdb.py
# 3. Quando estiver satisfeito:

git add .
git commit -m "adiciona filtro por gênero"
git push

# 4. Aguarda ~30 segundos
# 5. Acessa a URL — o app já está atualizado
```

---

## Referência rápida — Comandos Git

| Comando | Quando usar |
|---|---|
| `git init` | Uma vez, ao iniciar um projeto novo |
| `git remote add origin [url]` | Uma vez, para conectar ao GitHub |
| `git status` | Sempre que quiser ver o que mudou |
| `git add .` | Antes de todo commit |
| `git commit -m "mensagem"` | Para salvar um ponto de restauração |
| `git push` | Para enviar ao GitHub (e atualizar o app) |
| `git log --oneline` | Para ver o histórico de commits |

---

## Checklist de deploy

Antes de fazer o primeiro push, confirme:

- [ ] O arquivo `.gitignore` existe e contém `.streamlit/secrets.toml`
- [ ] O `requirements.txt` existe com `streamlit` e `requests`
- [ ] O app roda localmente sem erro (`streamlit run app_tmdb.py`)
- [ ] O `secrets.toml` **não aparece** no `git status` (deve ser ignorado)
- [ ] O repositório no GitHub foi criado como **Public**
- [ ] As secrets foram configuradas no painel do Streamlit Cloud

---

## O que acontece se eu subir a chave por acidente?

Acontece com todo mundo ao menos uma vez. O procedimento é:

1. Acesse **tmdb.org → configurações da conta → API** e **revogue imediatamente** o token comprometido
2. Gere um novo token
3. Atualize o `secrets.toml` local e as secrets no Streamlit Cloud
4. No GitHub, vá em Settings → Secrets scanning para verificar se o GitHub já detectou o vazamento

> 🧠 O motivo de revogar primeiro é que bots que varrem o GitHub são rápidos — você não tem tempo de apagar o arquivo antes que alguém copie a chave. Revogue, e mesmo que alguém copie, a chave não vai funcionar mais.

---

*Guia elaborado para turmas do ensino médio público — foco em publicar o projeto TMDB com segurança e ter uma URL pública para o portfólio.*
