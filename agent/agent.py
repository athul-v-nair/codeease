from langchain.tools import tool
from langchain.agents import  create_agent
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
from ai.vector_store import VectorStore
from core.watcher import watch_logs
from core.runner import re_run
from core.fixer import suggest_fix
from config.settings import HUGGINGFACEHUB_API_TOKEN
from agent.prompt import SYSTEM_PROMPT
class CodeEaseAgent:
    def __init__(self):
        self.db=VectorStore()
        
        # Initialize the main LLM for workflow automation
        self.llm = HuggingFaceEndpoint(
            repo_id="deepseek-ai/DeepSeek-R1-0528",
            task="text-generation",
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=1.03,
            provider="auto",  # let Hugging Face choose the best provider for you
        )
        self.chat_model = ChatHuggingFace(llm=self.llm)
        
        # Define tools for the agent
        self.tools = [
            tool(
                name_or_callable="WatchLogs",
                runnable=watch_logs,
                description="Runs the code initially and returns the log"
            ),
            tool(
                name_or_callable="SearchFixDB",
                runnable=self.db.search_fix,
                description="Searches database for similar past errors."
            ),
            tool(
                name_or_callable="SuggestFixLLM",
                runnable=suggest_fix,
                description="Uses LLM to suggest fixes for a given error log."
            ),
            tool(
                name_or_callable="StoreFixDB",
                runnable=lambda args: self.db.store_fix(
                    args["error"], args["fix"], args["explanation"]
                ),
                description="Stores a new fix and explanation into the vector database."
            ),
            # Will be added later
            # tool(
            #     name_or_callable="FileEditor",
            #     runnable=lambda args: self.editor.edit_code(args["file_path"], args["fix"]),
            #     description="Edits only affected lines in the code file."
            # ),
            tool(
                name_or_callable="RerunProgram",
                runnable=re_run,
                description="Re-runs the Python file after patching."
            )
        ]

        # Agent creation
        self.agent = create_agent(model=self.chat_model, tools=self.tools, system_prompt=SYSTEM_PROMPT)