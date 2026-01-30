from .gpt_client import GPTClient
from .claude_client import ClaudeClient

class ModelFactory:
    """Model selection factory"""
    @staticmethod
    def get_model(provider: str):
        if provider == "openai":
            return GPTClient()
        elif provider == "anthropic":
            return ClaudeClient()
        return None
