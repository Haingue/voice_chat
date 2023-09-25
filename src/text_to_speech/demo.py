import os
import time
from os.path import exists, join, basename, splitext
import sys

sys.path.append('TTS')
sys.path.append('WaveRNN')
from localimport import localimport

from IPython.display import Audio, display

# TTS
tts_pretrained_model = 'tts_models/checkpoint_261000.pth.tar'

tts_pretrained_model_config = 'tts_models/config.json'

#
# this code is copied from: https://github.com/mozilla/TTS/blob/master/notebooks/Benchmark.ipynb
#

import io
import torch
import time
import numpy as np
from collections import OrderedDict
from matplotlib import pylab as plt
import IPython
import librosa
import librosa.display

from TTS.models.tacotron import Tacotron
from TTS.layers import *
from TTS.utils.data import *
from TTS.utils.audio import AudioProcessor
from TTS.utils.generic_utils import load_config, setup_model
from TTS.utils.text import text_to_sequence
from TTS.utils.synthesis import synthesis
from TTS.utils.visual import visualize


def tts(model, text, CONFIG, use_cuda, ap, use_gl, speaker_id=None, figures=True):
    t_1 = time.time()
    waveform, alignment, mel_spec, mel_postnet_spec, stop_tokens = synthesis(model, text, CONFIG, use_cuda, ap,
                                                                             truncated=True,
                                                                             enable_eos_bos_chars=CONFIG.enable_eos_bos_chars)
    if CONFIG.model == "Tacotron" and not use_gl:
        mel_postnet_spec = ap.out_linear_to_mel(mel_postnet_spec.T).T
    if not use_gl:
        waveform = wavernn.generate(torch.FloatTensor(mel_postnet_spec.T).unsqueeze(0).cuda(), batched=batched_wavernn,
                                    target=11000, overlap=550)

    print(" >  Run-time: {}".format(time.time() - t_1))
    if figures:
        visualize(alignment, mel_postnet_spec, stop_tokens, text, ap.hop_length, CONFIG, mel_spec)
    IPython.display.display(Audio(waveform, rate=CONFIG.audio['sample_rate']))
    # os.makedirs(OUT_FOLDER, exist_ok=True)
    # file_name = text.replace(" ", "_").replace(".","") + ".wav"
    # out_path = os.path.join(OUT_FOLDER, file_name)
    # ap.save_wav(waveform, out_path)
    return alignment, mel_postnet_spec, stop_tokens, waveform


use_cuda = True
batched_wavernn = True

# initialize TTS
CONFIG = load_config(tts_pretrained_model_config)
from TTS.utils.text.symbols import symbols, phonemes

# load the model
num_chars = len(phonemes) if CONFIG.use_phonemes else len(symbols)
model = setup_model(num_chars, CONFIG)
# load the audio processor
ap = AudioProcessor(**CONFIG.audio)
# load model state
if use_cuda:
    cp = torch.load(tts_pretrained_model)
else:
    cp = torch.load(tts_pretrained_model, map_location=lambda storage, loc: storage)

# load the model
model.load_state_dict(cp['model'])
if use_cuda:
    model.cuda()
model.eval()
print(cp['step'])
model.decoder.max_decoder_steps = 2000

# initialize WaveRNN
VOCODER_CONFIG = load_config(wavernn_pretrained_model_config)
with localimport('/content/WaveRNN') as _importer:
    from models.wavernn import Model
bits = 10

wavernn = Model(
    rnn_dims=512,
    fc_dims=512,
    mode="mold",
    pad=2,
    upsample_factors=VOCODER_CONFIG.upsample_factors,  # set this depending on dataset
    feat_dims=VOCODER_CONFIG.audio["num_mels"],
    compute_dims=128,
    res_out_dims=128,
    res_blocks=10,
    hop_length=ap.hop_length,
    sample_rate=ap.sample_rate,
).cuda()
check = torch.load(wavernn_pretrained_model)
wavernn.load_state_dict(check['model'])
if use_cuda:
    wavernn.cuda()
wavernn.eval()
print(check['step'])

SENTENCE = 'Bill got in the habit of asking himself “Is that thought true?” And if he wasn’t absolutely certain it was, he just let it go.'

align, spec, stop_tokens, wav = tts(model, SENTENCE, CONFIG, use_cuda, ap, speaker_id=0, use_gl=False, figures=False)