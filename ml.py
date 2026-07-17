import os
from pathlib import Path
from dotenv import load_dotenv
from picoagents import Agent, OpenAIChatCompletionClient

load_dotenv(Path.cwd() / ".." / ".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is empty. Check your .env file path and contents.")

print("API key loaded successfully.")