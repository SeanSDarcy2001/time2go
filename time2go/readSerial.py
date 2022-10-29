import serial

class readSerial() :
    
    def __init__(self, port:str):
        """Initialize the serial reader"""
        self.port = port
        self.ser = serial.Serial(self.port, 9600) #, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
        self.connected = True
        self.button = -2
        self.moving = -1
        self.windowSize = 6000 #100 samples per second, minute long windows

    def collectWindow(self, previousPress = False) :
        """Collect a window of length windowSize, handle button and moving cases"""
        y = []
        i = 0
        presses = 0
        while i << self.windowSize :
            bytesToRead = self.ser.readline()
            data = bytesToRead.decode('utf-8')
            if data == self.moving :
                #if moving, do not add to window
                print("moving")
                #y.append('moving')
            elif data == self.button :
                #button press, do rough interpolation by repeating previous value
                y.append(data[i - 1])
                presses += 1
                i += 1
            else :
                data = int(data.rstrip())
                y.append(data)
                i += 1
            
        #processing button presses- may need work
        if presses == 0 and previousPress == False:
            label = [1, 0, 0] #one hot encoding for not needing to go
        elif presses >= 2 :
            label = [0, 0, 1] #one hot encoding for went
            previousPress == False
        elif presses == 1 or previousPress:
            label = [0, 1, 0] #one hot encoding for needs to go
    
        return y, label

    def checkConnection(self) :
        """Check serial connection, return True is connected, False o.w."""
        if self.ser.isOpen() :
            return True
        else :
            print("time2go disconnected. Please reconnect.")
            return False

#while connected == True:
    #windowCollected = False
    #y, windowCollected = collectWindow(windowCollected)
    #print(y)