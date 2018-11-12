import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(3,GPIO.OUT,initial=0)

GPIO.output(3,True)
