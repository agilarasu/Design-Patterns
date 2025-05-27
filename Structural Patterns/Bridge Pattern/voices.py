from abc import ABC, abstractmethod


class BaseTTS(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def speak(self, text):
        pass


class GoogleTTS(BaseTTS):
    def __init__(self):
        print("Google TTS initialized")

    def speak(self, text):
        print(f"Google TTS speaking: {text}")


class AzureTTS(BaseTTS):
    def __init__(self):
        print("Azure TTS initialized")

    def speak(self, text):
        print(f"Azure TTS speaking: {text}")
