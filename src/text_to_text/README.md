# [GPT4all](https://github.com/nomic-ai/gpt4all)

[Official Python Bindings](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md)

## Install
```commandline
pip install gpt4all
```

## Example
```python
from gpt4all import GPT4All

gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)
```