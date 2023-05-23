import os

model_name = "tts_models/fr/mai/tacotron2-DDC"


def read_text(input_text: str):
    # input_text = input_text.strip().replace("\"", "'")
    cmd = "tts --text \"%s\" --model_name \"%s\" >.\\env\\tts.log" % (input_text, model_name)
    print("CMD: %s" % cmd)
    os.system(cmd)
    return "tts_output.wav"
