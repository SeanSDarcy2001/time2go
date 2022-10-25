import numpy as np
from scipy.ndimage import uniform_filter1d


def runningMean(x, N) :
    """A moving average filter applied to a signal, x, with window size N"""
    y = uniform_filter1d(x, size=N)
    return y

def iterativeDownsample(x) :
    """Iterative downsampling of signal x to 2 Hz with LPF up to 1/4 of Nyquist or 1/8 of Baud"""
    #apply LPF 

def weinerFilter(x) :
    """Apply Weiner filter to remove baseline drift"""

def butterworthFilter(x) :
    """Butterworth filter with a cutoff of 9 cpm"""

def CWT(x) :
    """A continuous wavelet transform using a Morse wavelet"""