from langchain_openrouter import ChatOpenRouter
import os

# Defina sua chave de API
os.environ["OPENROUTER_API_KEY"] = "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"

# Crie o agente de chat
chat = ChatOpenRouter(
    model="qwen/qwen3.6-plus:free",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# Exemplo de uso
response = chat.invoke("Olá, OpenRouter! Quem é você?")
print(response.content)
