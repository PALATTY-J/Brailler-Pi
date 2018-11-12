import RPi.GPIO as GPIO
import time

def wait():
    if GPIO.input(5)==1:
        print ("ack rcvd")
        return
   


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(8,GPIO.OUT,initial=0)
GPIO.setup(3,GPIO.OUT,initial=0)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.LOW);
print ("p1")
wait()
GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.HIGH);
print ("p2")
wait()
GPIO.output(8,GPIO.HIGH);
GPIO.output(3,GPIO.LOW);
print ("p3")
wait()
GPIO.output(8,GPIO.HIGH);
GPIO.output(3,GPIO.HIGH);
print ("p4")
wait()
GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.LOW);
print ("p5")
wait()
GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.HIGH);
print ("p6")
wait()
    




