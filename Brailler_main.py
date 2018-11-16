import RPi.GPIO as GPIO
import time

def wait():   
    
    if GPIO.input(5)==0:
        print ("ack rcvd")

    return
   


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(8,GPIO.OUT,initial=0)
GPIO.setup(3,GPIO.OUT,initial=0)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.OUT,initial=0)


print("BEGIN OF TRANSMISSION")

GPIO.output(7,GPIO.HIGH)



GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.LOW);
print ("p1")
GPIO.wait_for_edge(5,GPIO.BOTH)

GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.HIGH);
print ("p2")



GPIO.output(8,GPIO.HIGH);
GPIO.output(3,GPIO.LOW);
print ("p3")



GPIO.output(8,GPIO.HIGH);
GPIO.output(3,GPIO.HIGH);
print ("p4")



GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.LOW);
print ("p5")



GPIO.output(8,GPIO.LOW);
GPIO.output(3,GPIO.HIGH);
print ("p6")



    

GPIO.output(7,GPIO.LOW)
print("END OF TRANSMISSION")



