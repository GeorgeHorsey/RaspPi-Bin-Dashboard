#Bulk of code is from
#https://forums.raspberrypi.com Member Username: pcmanbob
#Post https://forums.raspberrypi.com/viewtopic.php?t=208676 

#!/usr/bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)

# wait for button press loop 
while True:
    # waiting for door to open
    while GPIO.input(7) == 1:
        time.sleep(0.5)

    # log date and time for button press
    push = (time.strftime("%a %b %d %Y %H:%M:%S"))       
    with open("/home/pi/bin_time.txt", "a") as file: #date and time when an item is placed in bin  
        file.write(push + "\n")
    GPIO.output(8, GPIO.HIGH)
        
    while GPIO.input(7) == 0:
        time.sleep(0.5)  
    GPIO.output(8, GPIO.LOW)
    