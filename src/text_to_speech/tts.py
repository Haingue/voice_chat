import os

model_name = "tts_models/fr/mai/tacotron2-DDC"


def read_text(input_text: str):
    input_text = input_text.replace("\"", "'")
    input_text = input_text.replace("\r\n", " ")
    input_text = input_text.replace("\n", " ")
    input_text = input_text.strip()
    cmd = "tts --text \"%s\" --model_name \"%s\" >.\\env\\tts.log" % (input_text, model_name)
    print("CMD: %s" % cmd)
    os.system(cmd)
    return "tts_output.wav"
