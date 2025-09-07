"""
Integration service with GitHub API for accessing AI models (simplified version)
"""

import os
from typing import List, Dict, Optional
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.exceptions import AzureError


class GitHubModelsClient:
    def __init__(self, token: Optional[str] = None, endpoint: str = "https://models.github.ai/inference"):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.endpoint = endpoint
        self.model = "openai/gpt-4o-mini"
        self.client = ChatCompletionsClient(endpoint=self.endpoint, credential=self.token)

    async def chat_completion(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        # Convert messages to Azure format
        azure_messages = []
        for msg in messages:
            if msg.get("role") == "system":
                azure_messages.append(SystemMessage(content=msg["content"]))
            elif msg.get("role") == "user":
                azure_messages.append(UserMessage(content=msg["content"]))

        try:
            response = self.client.complete(
                model=self.model,
                messages=azure_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            # Azure response structure
            if response.choices and response.choices[0].message:
                return response.choices[0].message.content
            else:
                raise Exception("Resposta inesperada do modelo.")
        except AzureError as e:
            # Erro detalhado do Azure
            return f"Erro Azure AI Inference: {str(e)}"
        except Exception as e:
            # Fallback simulado para testes
            return f"[Simulado] Não foi possível obter resposta do modelo: {str(e)}"
