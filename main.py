"""
Created on Fri Oct 28 11:00:00 2022
@author: sdarcy2
"""

from time2go.readSerial import readSerial
from time2go.processingToolbox import processingToolbox
from time2go.eggDataset import eggDataset


def main() : 

    #initialize time2go serial reader
    print("Initializing time2go...")
    serial = readSerial('/dev/tty.HC-05-DevB')
    connected = serial.checkConnection()
    if connected :
        print("time2go connected!")
        firstSample = True
    else : print("Could not connect to time2go.")

    #initialize signal processing toolbox
    tools = processingToolbox()

    needsToGo = False #this is a parameter for collectWindow which allows the oneHot encoding process to track whther the user indicated needing to go previously
    
    while connected :
        window, label = serial.collectWindow(needsToGo) #get window

        if label == [0, 1, 0] :
            needsToGo = True #user has indicated that they need to go
        elif label == [0, 0, 1] :
            needsToGo = False #user has gone, no longer needs to go
    
        #window = tools.runningMedian(window) #apply moving median filter
        #window = tools.weinerFilter(window) #remove baseline drift with Weiner filter
        #window = tools.butterworthFilter(window) #second order lowpass butterworth filter with 9 cpm cutoff
        #cwt = tools.CWT(window) #apply continuous wavelet transform to signal
        cwt = tools.processData(window) #does all above

        if firstSample :
            dataset = eggDataset(cwt, label)
            firstSample = False
        else : dataset.expandDataset(cwt, label)

        connected = serial.checkConnection() #check connection before collecting another window
    
    print("Lost connection to time2go.")


if __name__ == "__main()__" :
    main()
main()
