from typing import List, Dict
from gpt4all import GPT4All

model_name = "ggml-mpt-7b-chat.bin"
model_path = "./data/models/llm"
default_pre_prompt: List[Dict] = [
    {
        "role": "system",
        "content": """### Instruction:
        Vous êtes un développeur et un créateur de logiciels expert.
        Vous parlez oralement.
        Assurez-vous de ne pas vous répétez.
        Assurez-vous d'être Soyez concis.
        Si vous listez des éléments, vous n'en mettez pas trop.
        Parfois, vous relancez l'utilisateur à la fin de votre réponse pour continuer une conversation.
        \n### Prompt: """
    }
]


def generate_pre_prompt():
    return default_pre_prompt


def initialize_ttt():
    return GPT4All(model_name, model_path)


def chat_completion(model: GPT4All, text_input: str, context: [] = generate_pre_prompt()):
    context.append({"role": "user", "content": text_input})
    response = model.chat_completion(context, default_prompt_header=False, default_prompt_footer=True, verbose=False)
    choice = response['choices'][0]['message']
    context.append(choice)
    return choice['content']
