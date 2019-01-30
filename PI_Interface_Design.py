import os
import time
import RPi.GPIO as GPIO
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()



os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/1.mp3")
time.sleep(0.1)
ser.write("s".encode())
GPIO.wait_for_edge(2,GPIO.FALLING)
os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/3.mp3")
time.sleep(0.1)
os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/2.mp3")
time.sleep(0.1)

    

