from huggingface_hub import InferenceClient
from config.settings import HUGGINGFACEHUB_API_TOKEN
from config.settings import EMBEDDING_MODEL

class EmbeddingModel:
    def __init__(self):
        self.client = InferenceClient(
            provider="hf-inference",
            api_key=HUGGINGFACEHUB_API_TOKEN,
        )
        self.model = EMBEDDING_MODEL
    
    def encode(self, text: str):
        try:
            result = self.client.feature_extraction(text=text, model=self.model).tolist()
            return result
        except Exception as e:
            print("Error:", e)
            return None