#!/usr/bin/env python

import RPi.GPIO as GPIO
import csv
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


newUser = input("Enter new user name (Firstname.Lastname): ")
existingUser = False

f = open("coffeeList.csv","r")
reader=csv.reader(f)
for row in reader:
    if newUser in row:
        existingUser = True
        print ("ERROR: User already existing!")
f.close()


if existingUser == False:
    with open('coffeeList.csv','a') as fd:
        fd.write(newUser + ",0")
        print("New user joined database!")
     


owner = "Owner: "
coffee = "\nCoffee: 0"
print("Now place your tag for writing...")

try:
        reader.write(owner+newUser+coffee)
        print("Completed.")

finally:
        GPIO.cleanup()
