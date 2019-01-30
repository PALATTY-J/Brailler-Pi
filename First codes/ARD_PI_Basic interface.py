import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(8,GPIO.OUT,initial=0)
GPIO.setup(3,GPIO.OUT,initial=0)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.OUT,initial=0)

while True:
    
    GPIO.output(8,True)
    GPIO.output(3,True)

    GPIO.output(7,True)


    
    



