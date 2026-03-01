import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    return index

def search(index, query_embedding, k=5):
    distances, indices = index.search(np.array(query_embedding), k)
    return indices[0]