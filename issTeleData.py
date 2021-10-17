import requests as rq
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value



#arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
#
#def write_read(x):
#    arduino.write(bytes(x, 'utf-8'))
#    time.sleep(0.05)
#    data = arduino.readline()
#    return data
#
#position = []
#
#while True:
#    response = rq.get("http://api.open-notify.org/iss-now.json").json()
#    longitude = float(response["iss_position"]["longitude"])
#    latitude = float(response["iss_position"]["latitude"])
#    position = [longitude, latitude]
#    value = write_read(position)
#    print(value)
#    time.sleep(1)
#
#

