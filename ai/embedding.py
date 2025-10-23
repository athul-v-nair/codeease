import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

class EmbeddingModel:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        )
        self.model = "sentence-transformers/all-MiniLM-L6-v2"
    
    def encode(self, text: str):
        try:
            result = self.client.feature_extraction(text=text, model=self.model).tolist()
            print(result)
            return result
        except Exception as e:
            print("Error:", e)
            return None

        
model = EmbeddingModel()
model.encode(text="Cannot convert str to int")