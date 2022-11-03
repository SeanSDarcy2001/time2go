from time2go.readSerial import readSerial
from time2go.processingToolbox import processingToolbox
from time2go.eggDataset import eggDataset
import matplotlib.pyplot as plt
import numpy as np
import pickle

def main() : 

    #initialize time2go serial reader
    print("Initializing time2go...")
    serial = readSerial('/dev/tty.HC-05-DevB')
    connected = serial.checkConnection()
    if connected :
        print("time2go connected!")
        firstSample = True
    else : print("Could not connect to time2go.")


    needsToGo = False #this is a parameter for collectWindow which allows the oneHot encoding process to track whther the user indicated needing to go previously
    
    i = 1

    while connected :
        window, label = serial.collectWindow(needsToGo) #get window

        if label == [0, 1] :
            needsToGo = True #user has indicated that they need to go
        elif label == [1, 0] :
            needsToGo = False #user has gone/no longer needs to go

        if needsToGo :
            with open("{}{}".format("data/need/", i), 'wb') as f:
                pickle.dump(window, f)
        elif needsToGo == False :
            with open("{}{}".format("data/noNeed/", i), 'wb') as f:
                pickle.dump(window, f)

        #else : dataset.expandDataset(cwt, label)

        connected = serial.checkConnection() #check connection before collecting another window
    
    print("Lost connection to time2go.")


if __name__ == "__main()__" :
    main()
main()