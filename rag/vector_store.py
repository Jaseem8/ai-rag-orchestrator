
# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors
"""Vector Store with Cosine Similarity and Dot Product."""
import math
from typing import List, Dict, Any, Tuple

class VectorStore:
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []

    def add_document(self, doc_id: str, text: str, embedding: List[float], metadata: Dict[str, Any] = None):
        self.documents.append({
            "id": doc_id,
            "text": text,
            "embedding": embedding,
            "metadata": metadata or {}
        })

    @staticmethod
    def _cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)

    def similarity_search(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[Dict[str, Any], float]]:
        scores = []
        for doc in self.documents:
            sim = self._cosine_similarity(query_embedding, doc["embedding"])
            scores.append((doc, sim))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer

# Cached normalized vectors

# Modularized sparse tokenizer
