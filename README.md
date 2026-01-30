
# AI Text Intelligence API 

API de análise de texto construída com **FastAPI**, focada em tarefas de **Processamento de Linguagem Natural (NLP)**, como:

- Análise de sentimento
- Classificação de texto
- Sumarização de texto

O projeto foi desenvolvido com uma arquitetura simples, modular e fácil de escalar, ideal para estudos, portfólio e projetos reais.

## 🖼️ Prints do Projeto em Funcionamento

Abaixo estão alguns prints reais da API em execução, utilizando a documentação interativa do **Swagger (FastAPI)**:

### 📌 Documentação Interativa (Swagger UI)
<img width="1281" height="692" alt="image" src="https://github.com/user-attachments/assets/0eb56b7a-f0b7-477f-abcb-2fbbb5e18294" />

---

### 📌 Endpoint de Análise de Sentimento (/sentiment)
<img width="1272" height="640" alt="image" src="https://github.com/user-attachments/assets/f6a7716c-7327-46b7-8f52-22206778f94c" />

---

### 📌 Resposta da API em Execução
<img width="1255" height="623" alt="image" src="https://github.com/user-attachments/assets/8756b66b-67af-4e1f-a470-faf86acd9c42" />
```

---



---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **OpenAPI / Swagger**

---

## 📂 Estrutura do Projeto

```

ai-text-intelligence-api/
│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── services/
│       ├── sentiment.py
│       ├── classifier.py
│       └── summarizer.py
│
├── venv/
├── requirements.txt
└── README.md

````

---

## ⚙️ Instalação e Execução

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/ai-text-intelligence-api.git
cd ai-text-intelligence-api
````

### 2️⃣ Crie e ative o ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute a aplicação

```bash
python -m uvicorn app.main:app --reload
```

---

## 📖 Documentação (Swagger)

Após iniciar o servidor, acesse:

* **Swagger UI:**
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **OpenAPI JSON:**
  👉 [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 🔌 Endpoints Disponíveis

### 🔹 POST `/sentiment`

Analisa o sentimento do texto enviado.

**Request:**

```json
{
  "text": "Eu adorei esse produto, é incrível"
}
```

**Response:**

```json
{
  "sentiment": "positivo",
  "score": 2
}
```

---

### 🔹 POST `/classify`

Classifica o texto em categorias pré-definidas.

**Request:**

```json
{
  "text": "Este artigo fala sobre tecnologia e programação"
}
```

**Response:**

```json
{
  "label": "tecnologia"
}
```

---

### 🔹 POST `/summarize`

Gera um resumo do texto enviado.

**Request:**

```json
{
  "text": "Texto longo que será resumido..."
}
```

**Response:**

```json
{
  "summary": "Resumo do texto."
}
```

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo:

* Praticar **FastAPI**
* Aplicar conceitos básicos de **NLP**
* Criar uma API organizada e documentada
* Servir como **projeto de portfólio**

---

## 🧠 Próximas Melhorias (Roadmap)

* Integração com modelos de Machine Learning
* Autenticação (JWT)
* Dockerização
* Testes automatizados
* Deploy em cloud (Railway / Render / AWS)

---

## 📄 Licença

Este projeto está sob a licença MIT.
