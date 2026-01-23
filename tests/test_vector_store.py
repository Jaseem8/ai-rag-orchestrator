from rag.vector_store import VectorStore

def test_cosine_ranking():
    store = VectorStore()
    store.add_document("doc1", "Python programming", [1.0, 0.0, 0.0])
    store.add_document("doc2", "Machine learning", [0.0, 1.0, 0.0])
    results = store.similarity_search([0.9, 0.1, 0.0], top_k=1)
    assert results[0][0]["id"] == "doc1"
