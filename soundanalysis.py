
import numpy as np

import struct
import pyaudio
from scipy.fftpack import fft

import sys

import _thread
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
        data_int = struct.unpack(str(2*self.CHUNK) + 'B', data)
        self.data_int = data_int
        print(len(data_int))
        print(data_int)

    def analyze(self):
        highbound = 255
        lowbound = 10
        ripenum = 0
        for i in self.data_int:
            if i <= highbound:
                if i >= lowbound:
                    ripenum += 1
        print(ripenum / len(self.data_int))


if __name__ == '__main__':
    audio_app = AudioStream()
    audio_out = PlayAudio()
    # audio_app.start()
    # audio_out.start()
    try:
        _thread.start_new_thread(audio_app.start(), ('thread-1', 2, ))
        _thread.start_new_thread(audio_out.start(), ('thread-2', 4, ))
    except:
        print("unable to start thread.")

    audio_app.analyze()



