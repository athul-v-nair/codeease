import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")