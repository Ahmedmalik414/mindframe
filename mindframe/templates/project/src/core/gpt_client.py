from .base_llm import BaseLLM

class GPTClient(BaseLLM):
    """OpenAI GPT integration"""
    def generate(self, prompt: str):
        # TODO: Implement OpenAI call
        return "GPT response"
