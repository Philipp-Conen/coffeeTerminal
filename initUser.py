#!/usr/bin/env python

import RPi.GPIO as GPIO
import csv
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


newUser = input("Enter new user name (Firstname.Lastname): ")


csv_file = csv.writer(open('coffeeList.csv', "w"), delimiter=",")
for row in csv_file:
    if newUser == row[1]:
         print ("ERROR: User already existing!")

    else:
        csv_file.writerow(newUser + ",0")
     


owner = "Owner: "
coffee = "\nCoffee: 0"
print("Now place your tag to write")

try:
        reader.write(owner+newUser+coffee)
        print("Done")

finally:
        GPIO.cleanup()
