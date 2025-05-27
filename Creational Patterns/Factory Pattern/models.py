from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def __init__(self, api_key):
        pass

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def delete_history(self):
        pass


class GeminiModel(BaseModel):
    def __init__(self, api_key):
        self.messages = []
        print(f"Connected to Gemini Model with {api_key=}")

    def send_message(self, message):
        self.messages.append(message)
        print("Message sent successfully")
    
    def delete_history(self):
        self.messages = []
        print("Message deleted successfully")
    
class LlamaModel(BaseModel):
    def __init__(self):
        self.messages = []
        print("Connected to local Llama server at default port")

    def send_message(self, message):
        self.messages.append(message)
        print("Message sent successfully")
    
    def delete_history(self):
        self.messages = []
        print("Message deleted successfully")
    