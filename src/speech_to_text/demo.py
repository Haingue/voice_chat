from whisper import whisper

model = whisper.load_model("base")
result = model.transcribe("/data/speech/example_1.wav")
print(result["text"])