# [GPT4all](https://github.com/nomic-ai/gpt4all)

[Official Python Bindings](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md)

## Install
```commandline
pip install gpt4all
```

## Example
```python
from gpt4all import GPT4All

gptj = GPT4All("ggml-text_to_text-j-v1.3-groovy")
messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)
```

## Models
- **[ggml-mpt-7b-chat.bin](https://gpt4all.io/models/ggml-mpt-7b-chat.bin)** (4.7Go)
- [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin) (3.6Go)
- [gpt4all-lora-quantized-linux-x86.bin](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-training/chat) (401Ko)