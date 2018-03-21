import pyaudio
import numpy as np

from soundanalysis import *

import os

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 10.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# Play sound
stream.write(samples)

if __name__ == '__main__':
    # Start Recorder, recorder stops on its own
    audio_app = AudioStream()
    audio_app.start()

    # Stop Sound
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Do analysis
    audio_app.analyze()