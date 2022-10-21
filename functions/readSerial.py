import serial
import numpy as np

ser = serial.Serial('/dev/tty.HC-05-DevB', 9600) #, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
connected = True
button = -2
moving = -1
windowSize = 100

def collectWindow(windowCollected) :
    while(windowCollected == False) :
        y = []
        for i in range(windowSize) :
            bytesToRead = ser.readline()
            data = bytesToRead.decode('utf-8')
            if data == moving :
                y.append('moving')
            elif data == button :
                y.append(data[i - 1])
            else :
                data = int(data.rstrip())
            #print(data)
                y.append(data)
            i += 1
        windowCollected = True
    return y, windowCollected

while connected == True:
    windowCollected = False
    y, windowCollected = collectWindow(windowCollected)
    print(y)