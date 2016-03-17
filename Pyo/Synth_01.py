from pyo import *
from SpringGridBlock import *
import math

class FMSynth:
    def __init__(self, length, octave, mul):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        self.mul = mul
        
        #1d lists because 2d lists crash the thing
        self.freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.amps = [SigTo(value=0, time=0.02, init=0) for i in range(self.size)]
        self.index = SigTo(value=1, time=0.05, init=1, mul=2)
        
        self.src = FM(carrier=self.freqs, ratio=2, index=self.index, mul=self.amps, add=0)
        self.pan = SPan(input=self.src, outs=2, pan=[0.25, 0.75], mul=1, add=0)
        self.clip = Clip(input=self.pan, min=-0.9, max=0.9, mul=self.mul, add=0)
        self.output = self.clip
        
        
    def UpdateHeights(self, heights, avg):
        self.heights = heights
        i = 0
        
        for x in range(self.length):
            for z in range(self.length):
                self.amps[i].setValue(self.heights[x][z] * 0.05)
                i += 1
                
        self.index.setValue(avg)
        
    def UpdateNotes(self, notes):
        
        i = 0
        for x in range(self.length):
            for z in range(self.length):
                self.freqs[i].setValue(midiToHz(notes[x][z] + 12 * self.octave))
                i += 1
                
        self.src.setCarrier(self.freqs)
        
    def GetOutput(self):
        return self.output
                
#############################################################
class WTSynth:
    def __init__(self, length, octave, mul):
        self.length = length
        self.size = self.length*self.length
        self.octave = octave
        self.mul = mul
        
        self.voices = 2
        self.heights = [[0.0 for x in range(self.length)] for z in range(self.length)]

        self.m1 = NewMatrix(width=self.length, height=self.length, init=self.heights)
        self.m2 = NewMatrix(width=self.length, height=self.length, init=self.heights)
        self.inter = SigTo(0, 0.04, 0)
 
        
        self.xfreq = [Randi(min=50 - 50*0.01, max=50 + 50*0.01, freq=5) for i in range(self.voices)]
        self.zfreq = [Randi(min=50 - 50*0.01, max=50 + 50*0.01, freq=5) for i in range(self.voices)]

        #+ ou - le mul autour du add
        self.x = Sine(freq=self.xfreq, mul=0.25, add=0.5)
        self.z = Sine(freq=self.zfreq, mul=0.25, add=0.5)
        
        self.ptr1 = MatrixPointer(matrix=self.m1, x=self.x, y=self.z, mul=1, add=0)
        self.ptr2 = MatrixPointer(matrix=self.m2, x=self.x, y=self.z, mul=1, add=0)
        self.ptr = Interp(self.ptr1, self.ptr2, self.inter)

        self.lpf = Biquadx(input=self.ptr, freq=4000, q=1, type=0, stages=4, mul=1, add=0)
        self.hpf = Biquadx(input=self.ptr, freq=50, q=2, type=1, stages=2, mul=1, add=0)
        
        self.clip = Clip(input=self.hpf, min=-0.9, max=0.9, mul=self.mul, add=0)

        self.output = self.clip
        
        
    def UpdateHeights(self, heights):

        for x in range(self.length):
            for z in range(self.length):
                self.heights[x][z] = heights[x][z]

        self.which = int(self.inter.get())
        
        if self.which == 0:
            self.m2.replace(self.heights)
        else:
            self.m1.replace(self.heights)
        
        self.inter.setValue(1 - self.which)


    def UpdateNotes(self, notes):
        self.freq = midiToHz(notes[0] + 12 * self.octave)
        
        for i in range(self.voices):
            self.xfreq[i].setMin(self.freq - self.freq * 0.01)
            self.xfreq[i].setMax(self.freq + self.freq * 0.01)
            self.zfreq[i].setMin(self.freq - self.freq * 0.01)
            self.zfreq[i].setMax(self.freq + self.freq * 0.01)

        self.x.setFreq(self.xfreq)
        self.z.setFreq(self.zfreq)
        
    def GetOutput(self):
        return self.output





