
import numpy as np

import struct
import pyaudio
from scipy.fftpack import fft

import sys

from School.softwareEngineering.AgbotRipeness.soundout import *


class AudioStream(object):
    def __init__(self):

        # pyaudio stuff
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )

    def start(self):
        data = self.stream.read(self.CHUNK)
        print(data)


if __name__ == '__main__':
    audio_app = AudioStream()
    audio_app.start()
    audio_out = PlayAudio()
    audio_out.start()


