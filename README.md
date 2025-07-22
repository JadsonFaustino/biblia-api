# 📖 API da Bíblia (Ave Maria)

API desenvolvida em **Python com FastAPI** para acesso à Bíblia Ave Maria em formato JSON. Permite listar livros, capítulos e versículos via HTTP.

## 🚀 Como executar

```bash
pip install fastapi uvicorn loguru
uvicorn main:app --reload
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

## ✅ Health Check

**GET** `/health`

```json
{
  "mensagem": "Serviço rodando"
}
```

---

## 📚 Listar todos os livros

**GET** `/livros`

Retorna todos os livros com nome, abreviação, quantidade de capítulos e testamento.

---

## 📖 Buscar um livro específico

**GET** `/livro/{nome, abreviação ou índice do livro}`

Pode ser:
- Nome completo (`/livro/Gênesis`)
- Abreviação (`/livro/Gn`)
- Índice (`/livro/1`)

---

## 📄 Buscar um capítulo

**GET** `/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}`

Exemplo: `/livro/Gn/capitulo/1`

---

## ✝ Buscar um versículo

**GET** `/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}/versiculo/{número do versículo}`

Exemplos: `/livro/Gn/capitulo/1/versiculo/1`

---

## ❗ Erros comuns

- `404`: Livro/Capítulo/Versículo não encontrado
- `400`: Parâmetros inválidos

---

## 📁 Estrutura esperada (JSON)

```json
{
  "1": {
    "nome": "Gênesis",
    "abreviacao": "Gn",
    "capitulos": [
      {
        "versiculos": [
          { "versiculo": 1, "texto": "No princípio, Deus criou o céu e a terra." }
        ]
      }
    ]
  }
}
```

---

## 📌 Créditos

O JSON da Bíblia Ave Maria foi obtido e adaptado a partir do repositório:  
👉 [https://github.com/fidalgobr/bibliaAveMariaJSON](https://github.com/fidalgobr/bibliaAveMariaJSON)

---
