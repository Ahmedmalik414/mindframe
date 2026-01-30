from .base_llm import BaseLLM

class ClaudeClient(BaseLLM):
    """Anthropic Claude client"""
    def generate(self, prompt: str):
        # TODO: Implement Anthropic call
        return "Claude response"
