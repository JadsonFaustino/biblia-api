# 📖 API da Bíblia

API desenvolvida em **Python com FastAPI** para acesso à Bíblia em formato JSON. Permite listar livros, capítulos e versículos via HTTP.

## 🚀 Como executar

```bash
pip install fastapi uvicorn loguru
uvicorn main:app --reload
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

## ✅ Health Check

**GET** `/biblia/health`

```json
{
  "mensagem": "Serviço rodando"
}
```

---

## 📚 Listar todos os livros

**GET** `/biblia/livros`

Retorna todos os livros com nome, abreviação, quantidade de capítulos e testamento.

---

## 📖 Buscar um livro específico

**GET** `/biblia/livro/{nome, abreviação ou índice do livro}`
**GET** `/biblia/{edicao}/livro/{nome, abreviação ou índice do livro}`

Pode ser:
- Nome completo (`/biblia/livro/Gênesis`)
- Abreviação (`/biblia/livro/Gn`)
- Índice (`/biblia/livro/1`)
- Com edição (`/biblia/pastoral/livro/gn`)

---

## 📄 Buscar um capítulo

**GET** `/biblia/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}`
**GET** `{edicao}/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}`

Exemplos: 
- `/biblia/livro/Gn/capitulo/1`
- `/biblia/ave-maria/livro/apocalipse/capitulo/5`

---

## ✝ Buscar um versículo

**GET** `/biblia/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}/versiculo/{número do versículo}`
**GET** `/biblia/{edicao}/livro/{nome, abreviação ou índice do livro}/capitulo/{número do capítulo}/versiculo/{número do versículo}`

Exemplos: 
- `/biblia/livro/Gn/capitulo/1/versiculo/1`
- `/biblia/pastoral/livro/deuteronomio/capitulo/10/versiculo/20`

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

O JSON da Bília Pastoral foi gerado a partir de Web Scrapping e consultas a API utilizada no site da Paulus:  
👉 [https://biblia.paulus.com.br/biblia-pastoral](https://biblia.paulus.com.br/biblia-pastoral)

O JSON da Bíblia de Aparecida foi gerado a partir de Web Scrapping e consultas a API utilizada no site da Bíblia de Aparecida:  
👉 [https://www.a12.com/biblia/](https://www.a12.com/biblia/)

---
