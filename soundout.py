import pyaudio
import wave
import sys


class PlayAudio(object):
    def __init__(self):
        self.CHUNK = 1024
        self.file = 'C:/Users/deser/Documents/Myfiles/School/softwareEngineering/AgbotRipeness/sound.wav'

    def start(self):
        if not self.file:
            print("Can't find wave file %s" % self.file)
            sys.exit(-1)

        wf = wave.open(self.file)

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(self.CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
