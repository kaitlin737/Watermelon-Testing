import pyaudio
import numpy as np
from soundanalysis import *
from threading import Thread


class PlaySound(object):
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.volume = 0.5     # range [0.0, 1.0]
        self.fs = 44100       # sampling rate, Hz, must be integer
        self.duration = 1.5   # in seconds, may be float
        self.f = 340.0        # sine frequency, Hz, may be float

    def startSound(self):
        # generate sample stream
        samples = (np.sin(2*np.pi*np.arange(self.fs*self.duration)*self.f/self.fs)).astype(np.float32).tobytes()

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = self.p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=self.fs,
                             output=True)
        stream.write(samples)
        stream.stop_stream()
        stream.close()
        self.p.terminate()


if __name__ == '__main__':
    # Create Objects.
    audio_play = PlaySound()
    audio_app = AudioStream()

    # Play Sound Wave
    Thread(target=audio_play.startSound())

    # Start Recorder, recorder stops on its own
    Thread(target=audio_app.start())

    # Do analysis
    audio_app.analyze()
