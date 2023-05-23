# from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
# processor = AutoProcessor.from_pretrained("openai/whisper-base")
# model = AutoModelForSpeechSeq2Seq.from_pretrained("openai/whisper-base")

import whisper

# model = whisper.load_model("../../data/models/stt/whisper-base/pytorch_model.bin")
model = whisper.load_model("base")
result = model.transcribe("data/dataset/speech/fr_micro_service.wav")
print(result["text"])
