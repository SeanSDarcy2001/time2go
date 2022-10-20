import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ser = serial.Serial('/dev/tty.HC-05-DevB', 9600) #, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
connected = True
button = 'b'
moving = 'n'

while connected == True:
    bytesToRead = ser.readline()
    print(bytesToRead.decode('utf-8'))

