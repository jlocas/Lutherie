from pyo import *
from SpringGridBlock import *
import math

class FMSynth:
    def __init__(self, length):
        self.length = length

        self.octave = 1
        self.freqs = [[SigTo(value=100, time=0.1, init=100) for x in range(self.length)] for z in range(self.length)]
        self.amps = [[SigTo(value=0, time=0.02, init=100) for x in range(self.length)] for z in range(self.length)]
        

        self.src = FM(carrier=100, ratio=2, index=1, mul=1, add=0)
        self.out = self.src
        

    def UpdateBlocks(self, blocks):
        for x in range(self.length):
            for z in range(self.length):
                self.amps[x][z].setValue(blocks[x][z].position.y * 0.1)
                
        self.src.setMul(self.amps)
        

    def UpdateFreqs(self, freqs):
        for x in range(self.length):
            for z in range(self.length):
                self.freqs[x][z].setValue(freqs[x][z])