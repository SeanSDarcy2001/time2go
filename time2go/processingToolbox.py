import numpy as np
from scipy import signal
from scipy.ndimage import uniform_filter1d

class processingToolbox() :

    def __init__(self):
        """Initialize the processing toolbox"""
        self.fs = 9600 #sampling rate
        self.butter = signal.butter(2, 0.15, fs=self.fs, output='sos')  #figure out what first param does, cutoff should be normalized by sampling rate, maybe not if iterativedownsample used
        self.wavelet = signal.morlet2(6000, 20)
        
    def runningMean(self, x, N) :
        """A moving average filter applied to a signal, x, with window size N"""
        filtered = uniform_filter1d(x, size=N)
        return filtered

    def runningMedian(self, x) :
        """A moving median filter applied to a signal x"""
        filtered = signal.medfilt(x) #can add N as kernel size
        return filtered

    def iterativeDownsample(self, x) :
        """Iterative downsampling of signal x to 2 Hz with LPF up to 1/4 of Nyquist or 1/8 of Baud"""
        #apply LPF 

    def weinerFilter(self, x) :
        """Apply Weiner filter to remove baseline drift"""
        filtered = signal.wiener(x)
        return filtered

    def butterworthFilter(self, x) :
        """Applies second order Butterworth filter with a cutoff of 9 cpm, or 0.15 Hz"""
        filtered = signal.sosfilt(self.butter, x)
        return filtered

    def CWT(self, x) :
        """A continuous wavelet transform using a Morse (Morlet in scipy???) wavelet"""
        transformed = signal.cwt(x, self.wavelet)
        return transformed

    def processData(self, window) :
        x = self.runningMedian(window) #apply moving median filter
        #x = self.weinerFilter(x) #remove baseline drift with Weiner filter
        #x = self.butterworthFilter(x) #second order lowpass butterworth filter with 9 cpm cutoff
        return(x)
        #cwt = self.CWT(x) #apply continuous wavelet transform to signal
        #return cwt