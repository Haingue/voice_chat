import wget
import os


stt_model = 'https://huggingface.co/openai/whisper-base/tree/main'
ttt_model = 'https://gpt4all.io/models/ggml-mpt-7b-chat.bin'

os.system("git clone %s /data/models/stt" % stt_model)
wget.download(ttt_model, '/data/models/ttt')
