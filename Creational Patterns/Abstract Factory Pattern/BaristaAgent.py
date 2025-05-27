from interfaces import LLM, TTS, Agent

class BaristaLLM(LLM):
    def __init__(self):
        print("Barista LLM uses Gemini model")
    
    def send_message(self, message):
        print(f'[Barista LLM] recieved {message=}')
    
    def show_history(self):
        print("Barista History")

class BaristaTTS(TTS):
    def __init__(self):
        print("Barista TTS uses Google TTS service")
    
    def speak(self, text):
        print("Barista Agent speaks!!")

class BaristaAgent(Agent):
    def create_llm(self):
        return BaristaLLM()
    
    def create_tts(self):
        return BaristaTTS()