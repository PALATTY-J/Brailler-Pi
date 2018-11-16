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


while True:
    print("BEGIN OF TRANSMISSION")

    GPIO.output(7,GPIO.HIGH)



    GPIO.output(8,GPIO.LOW);
    GPIO.output(3,GPIO.LOW);
    
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)

    GPIO.output(8,GPIO.LOW);
    GPIO.output(3,GPIO.HIGH);
    
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)





    GPIO.output(8,GPIO.HIGH);
    GPIO.output(3,GPIO.LOW);
  
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)




    GPIO.output(8,GPIO.HIGH);
    GPIO.output(3,GPIO.HIGH);
    
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)





    GPIO.output(8,GPIO.LOW);
    GPIO.output(3,GPIO.LOW);
    
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)






    GPIO.output(8,GPIO.LOW);
    GPIO.output(3,GPIO.HIGH);
    GPIO.wait_for_edge(5,GPIO.FALLING)
    time.sleep(0.001)




        

    GPIO.output(7,GPIO.LOW)
    print("END OF TRANSMISSION")



