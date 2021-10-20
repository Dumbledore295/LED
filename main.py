import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rdeca = 18

while True:
    GPIO.setup(rdeca,GPIO.OUT)
    print ("LED on")
    GPIO.output(rdeca,GPIO.HIGH)

    time.sleep(1)

    print ("LED off")
    GPIO.output(rdeca,GPIO.LOW)
    
    time.sleep(1)