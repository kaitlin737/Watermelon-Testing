import pygame
from time import sleep
def sound():
    pygame.mixer.init()
    print("init")
    pygame.mixer.music.load("home/pi/Desktop/beep.mp3")
    print("loaded")
    pygame.mixer.music.play()
    print("play")
    while pygame.mixer.music.get_busy() == True:
        
	continue
while True:
    sleep(15)
    print("sound")
    sound()
        
    
	
