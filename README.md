# 📚 RAG PDF Academic Chatbot

Sistema de perguntas e respostas sobre documentos acadêmicos utilizando **RAG (Retrieval-Augmented Generation)** com:

- 🔎 Sentence-Transformers (BGE Embeddings)
- 📦 FAISS (Vector Search)
- 🤖 Ollama (LLM local - Mistral / Llama3)
- 📄 PyMuPDF (Leitura de PDF)

Projeto 100% open source e executável localmente.

---

## 🧠 Arquitetura
PDF → Chunking → Embeddings (BGE) → FAISS Index
↓
Pergunta → Embedding → Busca Vetorial
↓
Contexto Recuperado → LLM → Resposta


O modelo **não é treinado** com o PDF.  
O conhecimento é injetado dinamicamente no prompt via recuperação vetorial.

---

## 🚀 Tecnologias Utilizadas

- `sentence-transformers`
- `BAAI/bge-small-en-v1.5`
- `FAISS`
- `Ollama`
- `Mistral / Llama3`
- `PyMuPDF`
- `Torch`

---

## 📂 Estrutura do Projeto

rag_pdf_bot/  
│  
├── data/  
│ └── artigos.pdf  
│  
├── src/  
│ ├── app.py  
│ ├── loader.py  
│ ├── chunking.py  
│ ├── embeddings.py  
│ ├── vector_store.py  
│ └── rag_pipeline.py  
│  
├── requirements.txt  
└── README.md  
  
---

## ⚙️ Instalação

### 1️⃣ Clone o repositório
git clone <seu-repo>
cd rag_pdf_bot

---

### 2️⃣ Crie ambiente virtual
python -m venv venv

Ativar:

Linux / WSL: source venv/bin/activate

Windows: venv\Scripts\activate

---

### 3️⃣ Instale dependências

---

### 4️⃣ Instale o Ollama

Baixe em:

https://ollama.com/download

Depois instale um modelo:
ollama pull mistral
ou
ollama pull llama3

---

## ▶️ Como Executar

Coloque seu PDF em:
data/artigos.pdf

Depois execute:
python src/app.py

Você verá:
Carregando PDF...
Dividindo em chunks...
Gerando embeddings...
Criando índice FAISS...
Pergunta:

Digite sua pergunta e o sistema responderá com base no documento.

---

## 🔥 Melhorias Implementadas

- ✅ Embeddings com BGE (melhor performance semântica)
- ✅ Similaridade por produto interno (cosine)
- ✅ Normalização de embeddings
- ✅ Prompt restritivo para evitar alucinação
- ✅ Estrutura modular

---

## 📊 Melhorias Futuras

- [ ] Persistência do índice FAISS
- [ ] Suporte a múltiplos PDFs
- [ ] Re-ranking com Cross-Encoder
- [ ] Interface Web (Streamlit)
- [ ] API REST (FastAPI)
- [ ] Avaliação automática (precision@k)
- [ ] Dockerização

---

## 🧠 Conceitos Aplicados

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Dense Embeddings
- Similaridade Semântica
- Prompt Engineering

---

## 📌 Observações

- O modelo roda **100% local**
- Nenhum dado é enviado para APIs externas
- Ideal para documentos acadêmicos e técnicos

---

## 👨‍💻 Autor

Desenvolvido por Wanderson Batista

---

## ⭐ Contribuições

Sinta-se livre para abrir issues ou sugerir melhorias.

---

## 📄 Licença

MIT License
