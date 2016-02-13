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
        self.output = self.src.out()
        
        
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
                
        self.src.setCarrier(self.freqs)
                

class WTSynth:
    def __init__(self, length, octave):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        
        self.heights = [[0.0 for x in range(self.length)] for z in range(self.length)]

        self.matrix = NewMatrix(width=self.length, height=self.length, init=self.heights).normalize()

        self.x = Sine(freq=[50,50], mul=1, add=0)
        self.z = Sine(freq=[50,50], mul=1, add=0)
        
        self.ptr = MatrixPointer(matrix=self.matrix, x=self.x, y=self.z, mul=0.2, add=0)
        self.output = self.ptr.out()
        
        
    def UpdateBlocks(self, blocks):
        self.blocks = blocks
        
        for x in range(self.length):
            for z in range(self.length):
                self.heights[x][z] = self.blocks[x][z].position.y

        self.matrix.replace(self.heights)
        
    def UpdateNotes(self, notes):
        self.freq = midiToHz(notes[0] + 12 * self.octave)
        self.randFreq = [Randi(min=self.freq - self.freq*0.01, max=self.freq + self.freq*0.01, freq=.1), Randi(min=self.freq - self.freq*0.01, max=self.freq + self.freq*0.01, freq=.1)]


        self.x = Sine(freq=self.randFreq, mul=1, add=0)
        self.z = Sine(freq=self.randFreq, mul=1, add=0)
        self.ptr.setX(self.x)
        self.ptr.setY(self.z)
        


#synman.UpdateBlocks(blocks)