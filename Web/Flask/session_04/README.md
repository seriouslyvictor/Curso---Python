# Session 04 - Forms & User Input (GET)

Esta pasta implementa a aula 4 do plano do curso: um Conversor Universal em Flask.

## Como rodar

No terminal, entre nesta pasta:

```powershell
cd session_04
flask --app app.py run --debug
```

Abra no navegador:

```text
http://127.0.0.1:5000
```

## O que observar durante a aula

- O formulario usa `method="GET"`.
- Depois de enviar, os dados aparecem na URL.
- O atributo `name="valor"` vira `request.args.get("valor")`.
- O atributo `name="tipo"` vira `request.args.get("tipo")`.
- A pagina tem estado vazio: ela nao tenta calcular antes do primeiro envio.
- A validacao com `try/except` evita erro tecnico quando alguem digita texto.

## Estrutura

```text
session_04/
  app.py
  templates/
    conversor.html
  static/
    css/
      style.css
```
