from factory import MyModelFactory

model = MyModelFactory.create_model("gemini")
model.send_message("Hello")
model.delete_history()