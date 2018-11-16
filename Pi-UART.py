# get the GPIO Library
import RPi.GPIO as GPIO
import serial
import time

#Open named port 
ser = serial.Serial ("/dev/ttyS0")    

# the input buttons
up = 7
down = 8

#Setting up the GPIO Pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()



#Set baud rate to 9600
ser.baudrate = 9600                     



while True:
    ser.write("10".encode())
    ser.close() 
