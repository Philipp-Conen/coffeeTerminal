#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

print("Ready for coffee checkin")

while True:

    try:
        id, text = reader.read()
        print(id)
        owner = (text.split("\n"))[0] 
        coffee = (text.split("\n"))[1]
        owner = (owner.split(": "))[1]
        coffee = (coffee.split(": "))[1]
        print("Owner: " + owner)
        print("Coffee: " + coffee)

        coffee = int(coffee) + 1
        with open('coffeeList.csv','w') as fd:
            for row in fd:
                if owner in row:
                    fd.write(owner + "," + coffee)
            fd.close()
        rfid.write("Owner: " + owner + "\n" + "Coffee: " + str(coffee))
        print("New: " + str(coffee))
    finally:
        GPIO.cleanup()

    time.sleep(5)
