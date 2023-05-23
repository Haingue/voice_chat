from IPython.display import Audio
import torch
import time
import IPython

from TTS.tts.layers import *

from TTS.utils.audio import AudioProcessor
from TTS.config import load_config
from TTS.tts.models import setup_model
from TTS.utils.synthesizer import synthesis
from TTS.tts.utils.visual import visualize
from TTS.tts.utils.text.characters import _phonemes, _other_symbols



# TTS
tts_pretrained_model = './data/models/tts/tts_models--fr--mai--tacotron2-DDC/model_file.pth'
tts_pretrained_model_config = './data/models/tts/tts_models--fr--mai--tacotron2-DDC/config.json'
CONFIG = load_config(tts_pretrained_model_config)
use_cuda = False


def tts(model, text, CONFIG, use_cuda, ap, use_gl, speaker_id=None, figures=True):
    t_1 = time.time()
    waveform, alignment, mel_spec, mel_postnet_spec, stop_tokens = synthesis(model, text, CONFIG, use_cuda, ap,
                                                                             truncated=True,
                                                                             enable_eos_bos_chars=CONFIG.enable_eos_bos_chars)
    if CONFIG.model == "Tacotron" and not use_gl:
        mel_postnet_spec = ap.out_linear_to_mel(mel_postnet_spec.T).T

    print(" >  Run-time: {}".format(time.time() - t_1))
    if figures:
        visualize(alignment, mel_postnet_spec, stop_tokens, text, ap.hop_length, CONFIG, mel_spec)
    IPython.display.display(Audio(waveform, rate=CONFIG.audio['sample_rate']))
    # os.makedirs(OUT_FOLDER, exist_ok=True)
    # file_name = text.replace(" ", "_").replace(".","") + ".wav"
    # out_path = os.path.join(OUT_FOLDER, file_name)
    # ap.save_wav(waveform, out_path)
    return alignment, mel_postnet_spec, stop_tokens, waveform

def initialize_tts ():
    ## load model config
    num_chars = len(_phonemes) if CONFIG.use_phonemes else len(_other_symbols)
    model = setup_model(num_chars, CONFIG)

    ## load the audio processor
    ap = AudioProcessor(**CONFIG.audio)

    ## load model state
    if use_cuda:
        cp = torch.load(tts_pretrained_model)
    else:
        cp = torch.load(tts_pretrained_model, map_location=lambda storage, loc: storage)

    ## load the model
    model.load_state_dict(cp['model'])
    if use_cuda:
        model.cuda()
    model.eval()
    print(cp['step'])
    model.decoder.max_decoder_steps = 2000
    return model, ap

model, ap = initialize_tts()
SENTENCE = 'Bill got in the habit of asking himself “Is that thought true?” And if he wasn’t absolutely certain it was, he just let it go.'
align, spec, stop_tokens, wav = tts(model, SENTENCE, CONFIG, use_cuda, ap, speaker_id=0, use_gl=False, figures=False)
