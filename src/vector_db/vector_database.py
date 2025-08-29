from typing import List, Any
import numpy as np

class VectorDatabase:
    def __init__(self):
        self.embeddings = []
        self.ids = []

    def add_embedding(self, embedding: List[float], id: Any):
        self.embeddings.append(embedding)
        self.ids.append(id)

    def retrieve_embedding(self, id: Any) -> List[float]:
        if id in self.ids:
            index = self.ids.index(id)
            return self.embeddings[index]
        else:
            raise ValueError("ID not found in the vector database.")

    def get_all_embeddings(self) -> List[List[float]]:
        return self.embeddings

    def clear(self):
        self.embeddings.clear()
        self.ids.clear()

    def __len__(self):
        return len(self.embeddings)

    def cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        dot_product = np.dot(vec_a, vec_b)
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot_product / (norm_a * norm_b)

    def find_most_similar(self, query_embedding: List[float], top_k: int = 5) -> List[tuple]:
        similarities = []
        for idx, embedding in enumerate(self.embeddings):
            sim = self.cosine_similarity(query_embedding, embedding)
            similarities.append((self.ids[idx], sim))
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]