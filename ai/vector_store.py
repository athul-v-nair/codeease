import chromadb
from ai.embedding import EmbeddingModel

# Global variable vector db name
VectorDBName="Errors_and_Fixes"

class VectorStore:
    def __init__(self):
        self.client=chromadb.PersistentClient(path='./db')
        self.collection=self.client.get_or_create_collection(VectorDBName)
        self.embedder=EmbeddingModel()

    def store_fix(self, error: str, fix: str, explanation: str):
        # Embed error, fix, and explanation
        error_embedding = self.embedder.encode(error)
        fix_embedding = self.embedder.encode(fix)
        explanation_embedding = self.embedder.encode(explanation)

        # Documents and metadatas for error, fix, and explanation
        documents = [
            f"Error: {error}",
            f"Fix: {fix}",
            f"Explanation: {explanation}"
        ]
        
        metadatas = [
            {"type": "error", "content": error},
            {"type": "fix", "content": fix},
            {"type": "explanation", "content": explanation}
        ]

        embeddings = [error_embedding, fix_embedding, explanation_embedding]

        self.collection.add(
            ids=[error[:50], fix[:50], explanation[:50]],  # Ensure each ID is unique
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
        return "Data embedding added to vector store."

    def search_fix(self, error: str, num_of_results:int=1):
        embedding=self.embedder.encode(error)
        result=self.collection.query(
            query_embeddings=[embedding],
            n_results=num_of_results
        )
        if result["documents"]:
            return [result["documents"][0][0], result["metadatas"][0][0]]
        else: 
            return None