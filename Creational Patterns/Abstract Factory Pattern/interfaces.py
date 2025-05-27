from abc import ABC, abstractmethod


# similar to typescript interfaces
class LLM(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def show_history(self):
        pass


class TTS(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def speak(self, text):
        pass


class Agent(ABC):
    @abstractmethod
    def create_llm(self):
        return LLM()

    @abstractmethod
    def create_tts(self):
        return TTS()
