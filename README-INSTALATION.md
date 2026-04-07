# Deep Agents – Instalação e Configuração (Ubuntu)

Este guia mostra o passo a passo para instalar e configurar o Deep Agents no Ubuntu, incluindo integração com Groq e OpenRouter.

## 1. Pré-requisitos
- Python 3.9+
- Git

## 2. Instalação do Python e dependências básicas
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

## 3. Clone o repositório Deep Agents
```bash
git clone https://github.com/langchain-ai/deepagents.git
cd deepagents
```

## 4. Crie e ative um ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 5. Instale o gerenciador uv
```bash
pip install uv
```

## 6. Instale as dependências do CLI
```bash
cd libs/cli
uv pip install -e .
```

## 7. Instale integrações de modelos (Groq e OpenRouter)
```bash
pip install langchain-groq langchain-openrouter
```

## 8. Configure a chave de API do Groq
```bash
export GROQ_API_KEY="sua_groq_api_key"
# Para tornar permanente:
echo 'export GROQ_API_KEY="sua_groq_api_key"' >> ~/.bashrc
```

## 9. Configure a chave de API do OpenRouter
```bash
export OPENROUTER_API_KEY="sua_openrouter_api_key"
# Para tornar permanente:
echo 'export OPENROUTER_API_KEY="sua_openrouter_api_key"' >> ~/.bashrc
```

## 10. Executando o Deep Agents CLI

### Usando Groq (exemplo com Llama 3 70B)
```bash
deepagents
```

> **Obs:** Alguns modelos do OpenRouter podem não ser reconhecidos diretamente pelo Deep Agents. Consulte a documentação ou use modelos amplamente suportados.

---

## Dicas
- Para listar modelos disponíveis na Groq:
  ```bash
  curl -H "Authorization: Bearer $GROQ_API_KEY" https://api.groq.com/openai/v1/models
  ```
- Para atualizar dependências:
  ```bash
  pip install -U deepagents langchain-groq langchain-openrouter
  ```

---

Para dúvidas ou erros, consulte a documentação oficial:
- [Deep Agents](https://github.com/langchain-ai/deepagents)
- [Groq Integration](https://docs.langchain.com/oss/python/integrations/chat/groq)
- [OpenRouter Integration](https://docs.langchain.com/oss/python/integrations/chat/openrouter)
