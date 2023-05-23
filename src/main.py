import numpy

from speech_to_text.stt import initialize_stt, transcribe
from text_to_speech.tts import read_text
from text_to_text.ttt import initialize_ttt, chat_completion, generate_pre_prompt
from utils.audio import listen_micro, play_wav
import time


def main():
    print("Initialize voice chat...")
    initialize_time = time.time()
    # input_path = "data/dataset/speech/fr_micro_service.wav"
    stt_model = initialize_stt()
    ttt_model = initialize_ttt()
    initialize_time = time.time() - initialize_time

    print("\n\nStart voice chat.............")
    # TODO detect key word in audio

    # loop in chat
    continue_chat = True
    context = generate_pre_prompt()
    chat_times = []
    while continue_chat:
        chat_time = time.time()
        # read audio from micro
        input_path = listen_micro()

        # Convert speech to text
        stt_output: str = transcribe(stt_model, input_path)
        print("\n\nTranscription: {0}".format(stt_output))

        ttt_output: str
        if stt_output.strip() == "Merci." or stt_output.strip() == "Thank you.":
            # Detect end of chat
            continue_chat = False
            ttt_output = 'A bientot !'
        else:
            # Generate answer
            ttt_output = chat_completion(ttt_model, stt_output, context)
        print("\n\nReflection: %s" % ttt_output)

        # Read answer
        try:
            # TODO don't save into file, play directly
            tts_output = read_text(ttt_output)
            print("\n\nSpeech: %s" % tts_output)

            play_wav(tts_output)
            print("\n\nReading speech: done")
        except Exception as error:
            print("\n\nError:")
            print(error)
        chat_time = time.time() - chat_time
        chat_times.append(chat_time)

    print("\n\nInitialize time: %ss" % initialize_time)
    print("Chat time avg: %ss" % numpy.mean(chat_times))
    print("End of voice chat, Bye Bye !")

if __name__ == "__main__":
    main()