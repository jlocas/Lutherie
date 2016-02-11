from pyo import *
from SpringGridBlock import *
import math

class FMSynth:
    def __init__(self, length, octave):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        
        #1d lists because 2d lists crash the thing
        self.freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.amps = [SigTo(value=0, time=0.02, init=0) for i in range(self.size)]
        

        self.src = FM(carrier=self.freqs, ratio=2, index=1, mul=self.amps, add=0)
        self.out = self.src
        self.out.out()
        
        
    def UpdateBlocks(self, blocks):
        self.blocks = blocks
        i = 0
        
        for x in range(self.length):
            for z in range(self.length):
                self.amps[i].setValue(self.blocks[x][z].position.y * 0.1)
                i += 1
                
        self.src.setMul(self.amps)
        
    def UpdateNotes(self, notes):
        
        i = 0
        
        for x in range(self.length):
            for z in range(self.length):
                self.freqs[i].setValue(midiToHz(notes[x][z] + 12 * self.octave))
                i += 1
                
#synman.UpdateBlocks(blocks)