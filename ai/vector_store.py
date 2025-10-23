import chromadb
from ai.embedding import EmbeddingModel

class VectorStore:
    def __init__(self):
        self.client=chromadb.Client()
        self.collection=self.client.get_or_create_collection("Errors_and_Fixes")
        self.embedder=EmbeddingModel()

    def store_fix(self, error: str, fix: str, explanation: str):
        embedding=self.embedder.encode(error)
        self.collection.add(
            ids=error[:50],
            documents=[f"{error}\n\nFix:\n{fix}\n\nExplanation:\n{explanation}"],
            embeddings=embedding,
            metadatas=[{"error": error, "fix": fix, "explanation": explanation}]
        )

    def search_fix(self, error: str, num_of_results:int=1):
        embedding=self.embedder.encode(error)
        result=self.collection.query(
            query_embeddings=[embedding],
            n_results=num_of_results
        )
        if result["documents"]:
            print(result)
            return [result["documents"][0][0], result["metadata"][0][0]]
        else: 
            return None