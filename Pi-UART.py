# get the GPIO Library
import RPi.GPIO as GPIO
import serial
import time

#Open named port 
ser = serial.Serial ("/dev/ttyS0")    



#Setting up the GPIO Pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(2,GPIO.IN)





#Set baud rate to 9600
ser.baudrate = 9600                     



while True:
    
    ser.write("x10".encode())
    
    GPIO.wait_for_edge(2,GPIO.FALLING)
    

    ser.write("y10".encode())
    GPIO.wait_for_edge(2,GPIO.FALLING)



    
    
