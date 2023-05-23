# Offline voice chat project
[Proof of concept in python]

## TODO list
- [X] Bind Whisper + GPT4all + Mozilla TTS (command)
- [X] Listen directly the micro
- [ ] Chat loop
  - [ ] Chat start detection
  - [X] Chat end detection
- [ ] Use TTS directly from python
- [ ] Add feature to detect the chat (like "OK Google !")
- [ ] Detect the end of chat

## Target
1. Start simple command or service
2. With the voice, start the transcription
3. Push the transcription in gpt4all (offline GPT)
4. Read the gtp4all's answer by generated voice

## Tools
- [Whisper](https://github.com/openai/whisper)
- [GPT4all](https://github.com/nomic-ai/gpt4all)
- [Mozilla TTS](https://github.com/mozilla/TTS)

## Resource
- [Talk.cpp](https://github.com/ggerganov/whisper.cpp/tree/master/examples/talk)