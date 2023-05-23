from typing import List, Dict
from gpt4all import GPT4All

gptj = GPT4All("ggml-mpt-7b-chat.bin", "./data/models/llm")

# Create the pre-prompt
messages: List[Dict] = [
    {
        "role": "system",
        "content": """### Instruction:
        The prompt below is a question to answer, a task to complete, or a conversation to respond to or engage in; decide which and write an appropriate response. Carefully read the prompt and provide a thoughtful and relevant response. Be sure to:

        - You are a developer and an expert software creator.
        - You talk orally.
        - Never repeat yourself and be concise.
        - If you list elements, you don't put too many.
        - Sometimes, you raise the user at the end of your answer to continue a conversation.
        \n### Prompt: """
    }
]

# Get the user sentence
messages.append({"role": "user", "content": "How create a program for IoT ?"})

# Run the prompt
response = gptj.chat_completion(messages, default_prompt_header=False, default_prompt_footer=True, verbose=True)
print(response)
print("")
print("")
print("Result:")
print(response['choices'][0]['message']['content'])
