from interfaces import LLM, TTS, Agent

class HealthLLM(LLM):
    def __init__(self):
        print("Health LLM uses LLama")
    
    def send_message(self, message):
        print(f'[Health LLM] recieved {message=}')
    
    def show_history(self):
        print("Health History")


class HealthTTS(TTS):
    def __init__(self):
        print("Health TTS uses Google TTS service")
    
    def speak(self, text):
        print("Health Agent speaks!!")

class HealthAgent(Agent):
    def create_llm(self):
        return HealthLLM()
    
    def create_tts(self):
        return HealthTTS()