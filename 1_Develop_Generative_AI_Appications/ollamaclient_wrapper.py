from langchain_ollama import ChatOllama


class ChatOllamaWrapper:
    def __init__(self, model="mistral", temperature=0.3, max_tokens=150, top_p=0.9):
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

    def createInstance(self):
        return ChatOllama(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
        )
