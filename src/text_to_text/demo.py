from gpt4all import GPT4All

gptj = GPT4All("ggml-text_to_text-j-v1.3-groovy")
messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)