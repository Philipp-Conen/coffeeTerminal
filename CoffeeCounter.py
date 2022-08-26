#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import csv
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

print("Ready for coffee checkin")

while True:

    try:
        id, text = rfid.read()
        print(id)
        owner = (text.split("\n"))[0] 
        coffee = (text.split("\n"))[1]
        owner = (owner.split(": "))[1]
        coffee = (coffee.split(": "))[1]
        print("Owner: " + owner)
        print("Coffee: " + coffee)

        coffee = int(coffee) + 1

        with open('coffeeList.csv') as inf:
            reader = csv.reader(inf.readlines())

        with open('coffeeList.csv', 'w') as outf:
            writer = csv.writer(outf)
            for line in reader:
                if owner in line:
                    writer.writerow(owner + "," + coffee)
                    break
                else:
                    print("ERROR: Not found!")


        rfid.write("Owner: " + owner + "\n" + "Coffee: " + str(coffee))
        print("New: " + str(coffee))
    finally:
        GPIO.cleanup()

    time.sleep(5)
