# [Whisper](https://github.com/openai/whisper)

## Install
```commandline
pip install TTS
```

## Example
```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```
[Python transcribe](https://medium.com/codingthesmartway-com-blog/voice-to-text-made-easy-implementing-a-python-app-with-openais-whisper-speech-to-text-api-e8f415a5f737)
[Whisper.cpp](https://github.com/ggerganov/whisper.cpp/tree/master/examples/command)
