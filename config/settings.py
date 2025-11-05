import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACEHUB_API_TOKEN=os.getenv("HUGGINGFACEHUB_API_TOKEN")
CODING_ASSISTANT_MODEL= "deepseek-ai/DeepSeek-V3.2-Exp"
EMBEDDING_MODEL= "sentence-transformers/all-MiniLM-L6-v2"