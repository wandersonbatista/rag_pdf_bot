
from sentence_transformers import SentenceTransformer

#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def embed_texts(texts):
    return model.encode(texts, normalize_embeddings=True)

def embed_query(query):
    instruction = "Represent this sentence for searching relevant passages: "
    return model.encode([instruction + query], normalize_embeddings=True)