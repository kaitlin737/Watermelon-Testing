
import numpy as np
import struct
import pyaudio
from scipy.fftpack import fft
import sys
import _thread


class AudioStream(object):
    def __init__(self):

        # pyaudio stuff
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 # * 2

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
        data_int = np.array(struct.unpack(str(2*self.CHUNK) + 'B', data), dtype='b')[::2] # + 255
        self.data_int = data_int
        print("Recorded for", len(data_int), "miliseconds")
        print(*data_int)

    def analyze(self):
        highbound = 100
        lowbound = -100
        ripenum = 0
        for i in self.data_int:
            if i <= highbound:
                if i >= lowbound:
                    ripenum += 1
        print(ripenum / len(self.data_int))


if __name__ == '__main__':
    audio_app = AudioStream()
    audio_app.start()
    audio_app.analyze()



