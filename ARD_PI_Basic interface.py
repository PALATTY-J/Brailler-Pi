import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(3,GPIO.OUT,initial=0)

while True:
    GPIO.output(3,False)
    time.sleep(.1)
    GPIO.output(3,True)
    time.sleep(1)
    



