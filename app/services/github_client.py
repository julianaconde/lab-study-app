"""
Integration service with GitHub API for accessing AI models (simplified version)
"""
import os
import requests
from typing import List, Dict, Optional
import json

class GitHubModelsClient:
    def __init__(self, token: Optional[str] = None, base_url: str = "https://models.inference.ai.azure.com"):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.base_url = base_url.rstrip("/")

    # Keeping the asynchronous signature for compatibility
    async def chat_completion(self, messages: List[Dict], temperature: float = 0.7, max_tokens: int = 2000) -> str:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        payload = {
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        try:
            resp = requests.post(
                f"{self.base_url}/gpt-4o/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response:
                raise Exception(f"API Error: {e.response.status_code}")
            else:
                raise Exception(f"Request failed: {str(e)}")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")
