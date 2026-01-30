class BaseLLM:
    """Common interface for all LLMs"""
    def generate(self, prompt: str):
        pass
