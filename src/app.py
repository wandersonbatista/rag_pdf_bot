# app.py
from loader import load_pdf
from embeddings import embed_texts, embed_query
from vector_store import create_faiss_index, search
from rag_pipeline import generate_answer
from chunking import chunk_text
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pdf_path = os.path.join(BASE_DIR, "data", "artigos.pdf")

print("Carregando PDF...")
text = load_pdf(pdf_path)

print("Dividindo em chunks...")
chunks = chunk_text(text)

print("Gerando embeddings...")
embeddings = embed_texts(chunks)

print("Criando índice FAISS...")
index = create_faiss_index(embeddings)

while True:
    question = input("\nPergunta: ")

    query_embedding = embed_query(question)
    relevant_indices = search(index, query_embedding, k=7)

    context = "\n".join([chunks[i] for i in relevant_indices])

    answer = generate_answer(context, question)

    print("\nResposta:", answer)