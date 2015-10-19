#!/usr/bin/env python
# encoding: utf-8
from pyo import *

class SpringGridSynth:
    def __init__(self, length=4):
        self.length = length
        self.size = self.length*self.length
        self.fundFreq = 50
        self.freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.freqBank = [0 for i in range(self.size)]
        self.amps = [SigTo(value=0, time=0.1, init=0) for i in range(self.size)]
        
    def SetFreqs(self):
        i=0
        for x in range(self.length):
            for z in range(self.length):
                self.freqs[i].setValue(self.fundFreq + self.fundFreq * (x + z))
                self.freqBank[i] = self.fundFreq + self.fundFreq * (x + z)
                i += 1