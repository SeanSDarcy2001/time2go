from time2go.readSerial import readSerial

print("Initializing time2go...")
serial = readSerial('/dev/tty.HC-05-DevB')
connected = serial.checkConnection()
if connected :
    print("time2go connected!")
    firstSample = True
else : print("Could not connect to time2go.")

needsToGo = False #this is a parameter for collectWindow which allows the oneHot encoding process to track whther the user indicated needing to go previously
print("NEEDS TO GO:", needsToGo)    

while connected :
        window, label, connected = serial.collectWindow(needsToGo) #get window

        if label == [0, 1] :
            needsToGo = True #user has indicated that they need to go
        elif label == [1, 0] :
            needsToGo = False #user has gone/no longer needs to go

        print("NEEDS TO GO:", needsToGo)  
