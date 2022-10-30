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
    
    while connected :
        window, label = serial.collectWindow(needsToGo) #get window
        
        
 

        if firstSample :
            with open('sampleWindow2.pkl', 'wb') as f:
                pickle.dump(window, f)
            firstSample = False
        #else : dataset.expandDataset(cwt, label)

        connected = serial.checkConnection() #check connection before collecting another window
    
    print("Lost connection to time2go.")


if __name__ == "__main()__" :
    main()
main()