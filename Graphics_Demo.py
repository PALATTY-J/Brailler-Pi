import os
import time
import RPi.GPIO as GPIO
import serial

ser = serial.Serial ("/dev/ttyS0")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(2,GPIO.IN)

ser.baudrate = 9600

os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/1.mp3")
time.sleep(0.1)
ser.write("s".encode())
GPIO.wait_for_edge(2,GPIO.FALLING)
os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/3.mp3")
time.sleep(0.1)
os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/2.mp3")
time.sleep(0.1)
os.system("omxplayer --vol +940 /home/pi/Brailler-Pi/5.mp3")
time.sleep(0.1)



y=0

while(y<=20):
    ser.write("z01".encode())
    GPIO.wait_for_edge(2,GPIO.FALLING)
    y=y+1


y=0

while (y<=50):

    for x in range(y):
        
        ser.write("z01".encode())
        GPIO.wait_for_edge(2,GPIO.FALLING)

        ser.write("f".encode())
        GPIO.wait_for_edge(2,GPIO.FALLING)
        ser.write("x25".encode())
        GPIO.wait_for_edge(2,GPIO.FALLING)
    x=0
    for x in range(y):
        ser.write("r".encode())
        GPIO.wait_for_edge(2,GPIO.FALLING)
        ser.write("x25".encode())
        GPIO.wait_for_edge(2,GPIO.FALLING)
        
    
    ser.write("y01".encode())
    GPIO.wait_for_edge(2,GPIO.FALLING)

    ser.write("z01".encode())
    GPIO.wait_for_edge(2,GPIO.FALLING)
    x=x+1

    

   
