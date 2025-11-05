import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

def suggest_fix(logs: str):
    if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
        return

    try:
        client = InferenceClient(
            provider="novita",
            api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        )  

        # Build prompt
        user_prompt=f"The following error occurred:\n{logs}\nPlease suggest the best corrected code. Please explain why this happened and how to avoid it in minimal words. The output must me in this format Proposed Fix:(Write the correct code here), Error:(Provide the main error here),Explanation: (Provide small explanation on how to fix it)"

        # Setting the behaviour
        messages = [
            {"role": "system", "content": "You are an AI coding assistant that fixes and explains code."},
            {"role": "user", "content": user_prompt}
        ]
        
        # Calling the model
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2-Exp",
            messages=messages
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Fixer failed: {e}"
