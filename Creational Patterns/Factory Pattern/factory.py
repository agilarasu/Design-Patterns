from models import GeminiModel, LlamaModel

class MyModelFactory():
    def create_model(model_name):
        if model_name == "gemini":
            return GeminiModel(api_key="")
        elif model_name == "llama":
            return LlamaModel()
        else:
            raise ValueError("Model Not defined")