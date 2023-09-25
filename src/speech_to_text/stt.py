import whisper

stt_model_type = "base"


def initialize_stt():
    return whisper.load_model(stt_model_type)


def transcribe(model, wav_file):
    result = model.transcribe(wav_file)
    return result["text"]
