# [Whisper](https://github.com/openai/whisper)

## Install
```commandline
pip install openai pyaudio wave
pip install git+https://github.com/openai/whisper.git
```
```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
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

## Models
- [Base](https://huggingface.co/openai/whisper-base/tree/main) (440Mo)