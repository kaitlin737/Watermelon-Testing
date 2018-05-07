#! /usr/bin/python
import pyaudio
import numpy as np
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)


class PlaySound(object):
	def __init__(self):
		self.p = pyaudio.PyAudio()
		self.volume = 1.0        # range [0.0, 1.0]
		self.fs = 48000          # sampling rate, Hz, must be integer
		self.duration = .2      # in seconds, may be float
		self.f = 400.0           # sine frequency, Hz, may be float

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
	while True:
		state = GPIO.input(11)
		#sleep(1)
		print(state)
		if state == 1:
			# Create Objects.
			audio_play = PlaySound()
			# Play Sound Wave
			audio_play.startSound()
			state = GPIO.input(11)
			#sleep(2)

                                                                         
