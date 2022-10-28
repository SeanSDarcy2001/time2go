"""
Created on Fri Oct 28 11:00:00 2022
@author: sdarcy2
"""

from functions import readSerial, processingToolbox, eggDataset

def main() : 

    #initialize time2go serial reader
    print("Initializing time2go...")
    serial = readSerial()
    connected = serial.checkConnection()
    if connected :
        print("time2go connected!")
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
    
        window = tools.runningMedian(window) #apply moving median filter
        window = tools.weinerFilter(window) #remove baseline drift with Weiner filter
        window = tools.butterworthFilter(window) #second order lowpass butterworth filter with 9 cpm cutoff
        cwt = tools.CWT(window) #apply continuous wavelet transform to signal

        



    

if __name__ == "__main()__" :
    main()
main()
