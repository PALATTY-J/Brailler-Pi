import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(23,GPIO.OUT)

#os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/1.mp3")
#time.sleep(0.1)
#os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/2.mp3")
#time.sleep(0.1)
while True:
    GPIO.output(23,1)
    time.sleep(0.1)
    GPIO.output(23,0)
    

