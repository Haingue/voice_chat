import os

model_name = "tts_models/fr/mai/tacotron2-DDC"


def read_text(input_text: str):
    input_text = input_text.replace("\"", "'").replace("\n", " ")
    os.system("tts --text \"{0}\" --model_name {1} >.\\env\\tts.log".format(input_text, model_name))
