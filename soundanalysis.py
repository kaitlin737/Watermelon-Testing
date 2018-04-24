
import numpy as np
import struct
import pyaudio
from scipy.fftpack import fft
import sys
from sense_hat import SenseHat
from time import sleep 
sense=SenseHat()
sense.clear()
X=[255,0,0]
O=[33,255,92]
ripe=[
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O,
O,O,O,O,O,O,O,O
]
not_ripe=[
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X
]
class AudioStream(object):
    def __init__(self):

    # pyaudio stuff
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024# * 2

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
        data_int = np.array(struct.unpack(str(2*self.CHUNK) + 'B', data), dtype='b')[::2]
        self.data_int = data_int
        print("Recorded for", len(data_int), "miliseconds")
        print(data_int)
    def stop(self):
        data=self.stream.close()

    def analyze(self):
        highbound = 20
        lowbound = 0
        ripenum = 0
        for i in self.data_int:
            if i <= highbound:
                if i >= lowbound:
                    ripenum += 1
        print(ripenum / len(self.data_int))
        if (ripenum / len(self.data_int)) == 0:
            sense.set_pixels(ripe)
            sleep(3)
            sense.clear()
            
        else:
            sense.set_pixels(not_ripe)
            sleep(3)
            sense.clear()

def program():
    running=True
    while running:
            for event in sense.stick.get_events():
                    if event.action == "pressed":
                            if event.direction == "middle":
                               audio_app = AudioStream()
                               audio_app.start()
                               print(" end start\n")
                               audio_app.analyze()
                               print("end analyze\n")
                               audio_app.stop()
                               running=False
    program()

if __name__ == '__main__':
    program()
    