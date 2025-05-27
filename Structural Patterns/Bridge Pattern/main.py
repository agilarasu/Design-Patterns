from models import BaseModel, GeminiModel, LlamaModel
from voices import BaseTTS, GoogleTTS, AzureTTS


# Assistant abstraction that bridges LLM and TTS
class Assistant:
    def __init__(self, model: BaseModel, tts: BaseTTS):
        self.model = model
        self.tts = tts

    def chat(self, message):
        self.model.send_message(message)
        self.tts.speak(message)

    def clear_history(self):
        self.model.delete_history()


# Create model and TTS instances
gemini_model = GeminiModel(api_key="gemini-1234")
llama_model = LlamaModel()

google_tts = GoogleTTS()
azure_tts = AzureTTS()

# Create assistants with different combos
assistant1 = Assistant(gemini_model, google_tts)
assistant2 = Assistant(llama_model, azure_tts)

# Use them
assistant1.chat("Hello from Gemini + Google")
assistant2.chat("Hello from Llama + Azure")

# Clear history
assistant1.clear_history()
assistant2.clear_history()
