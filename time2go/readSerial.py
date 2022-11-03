import serial

class readSerial() :
    
    def __init__(self, port:str):
        """Initialize the serial reader"""
        self.port = port
        self.ser = serial.Serial(self.port, 9600) #, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
        self.connected = True
        self.button = "1200"
        self.moving = "1100"
        self.windowSize = 1500 #100 samples per second, 5 second long windows minute long windows
        #altered to 300 samples a second for 10 second windows

    def collectWindow(self, previousPress = False) :
        """Collect a window of length windowSize, handle button and moving cases"""
        ch1 = []
        ch2 = []
        ch3 = []
        channel = 0
        presses = 0

        i = 0 #indicator for channel 1 size
        j = 0 #indicator for channel 2 size
        k = 0 #indicator for channel 3 size
       
        while i < self.windowSize and j < self.windowSize and k < self.windowSize and self.connected:
            #print("reading")
            bytesToRead = self.ser.readline()
            #print("passed readline")
            data = bytesToRead.decode('utf-8')

            data = data.strip()
            print(data)
            

            #figure out what channel data belongs to
            channel, data = self.whichData(data)

            #data = int.from_bytes(bytesToRead, 'big', signed = "True")
            #print(data)

            if data == self.moving :
                #if moving, do not add to window
                print("moving")
                #y.append('moving')
            elif data == self.button :
                print("PRESS RECEIVED")
                #button press, do rough interpolation by repeating previous value
                #y.append(data[i - 1])
                presses += 1
                #i += 1
            else :
                #data = int(data.rstrip())
                if channel == 1 :
                    ch1.append(data)
                    i = i + 1
                elif channel == 2 :
                    ch2.append(data)
                    j = j + 1
                elif channel == 3 :
                    ch3.append(data)
                    k = k + 1

            self.connected = self.checkConnection()
            
        #processing button presses- may need work
        if presses == 0 and previousPress == False:
            label = [1, 0] #one hot encoding for not needing to go
        elif presses >= 2 :
            label = [1, 0] #one hot encoding for went
            #previousPress == False
        elif presses == 1 or previousPress:
            label = [0, 1] #one hot encoding for needs to go
    
        y = [ch1, ch2, ch3]

        return y, label, self.connected

    def whichChannel(self, data) :
        """Check what channel data belongs to- return channel, data"""
        channelData = data.split(':')
        if channelData[0] == "C1" :
            channel = 1
        elif channelData[0] == "C2" :
            channel = 2
        elif channelData[0] == "C3" :
            channel = 3

        return channel, channelData[1]

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