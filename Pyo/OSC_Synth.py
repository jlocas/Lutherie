#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *
import math

class SpringGridSynth:
    def __init__(self, length=4):
        self.tonic = Sig(0)
        self.fundFreq = MToF(self.tonic)
        
        self.length = length
        self.size = self.length*self.length
    
        self.freqBank = [[0 for x in range(self.length)] for z in range(self.length)]
        self.midi = RawMidi(self.UpdateNotes)


        self.posInst_octave = 3
        self.posInst_freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.posInst_freqBank = [[0 for x in range(self.length)] for z in range(self.length)]        
        self.posInst_amps = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)]
        self.posInst = Sine(freq=self.posInst_freqs, mul=self.posInst_amps)
        
        self.velInst_octave = 5
        self.velInst_freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.velInst_freqBank = [[0 for x in range(self.length)] for z in range(self.length)]        
        self.velInst_amps = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)]
        self.velInst = Sine(freq=self.velInst_freqs, mul=self.velInst_amps)
        
        self.fm_octave = 3
        self.fm_freqs = [SigTo(value=100, time=0.1, init=100) for i in range(self.size)]
        self.fm_freqBank = [[0 for x in range(self.length)] for z in range(self.length)] 
        self.fm_amps = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)]
        self.fm_indices = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)]
        self.fm = FM(carrier=self.fm_freqs, index=self.fm_indices, ratio= [random.uniform(1.98, 2.02) for i in range(self.size)], mul = self.fm_amps)

        self.debug = False
        
        self.SetBaseFreqs()
        self.out()
        

    def Update(self, blocks):
        
        self.blocks = blocks

        i = 0
        for x in range(self.length):
            for z in range(self.length):
                self.posInst_amps[i].setValue(blocks[x][z].position.y * 0.1)
                self.posInst_freqs[i].setValue(self.posInst_freqBank[x][z])
                
                self.velInst_amps[i].setValue(blocks[x][z].velocity.y * 0.3)
                self.velInst_freqs[i].setValue(self.velInst_freqBank[x][z])
                
                self.fm_amps[i].setValue(blocks[x][z].position.y * 0.1)
                self.fm_freqs[i].setValue(self.fm_freqBank[x][z])
                self.fm_indices[i].setValue(blocks[x][z].velocity.y * 2)
                

                i += 1
        
        self.posInst.setFreq(self.posInst_freqs)
        self.posInst.setMul(self.posInst_amps)
        
        self.velInst.setFreq(self.velInst_freqs)
        self.velInst.setMul(self.velInst_amps)
        
        self.fm.setCarrier(self.fm_freqs)
        self.fm.setMul(self.fm_amps)
        self.fm.setIndex(self.fm_indices)
        #self.Debug()
                
    def SetBaseFreqs(self):

        for x in range(self.length):
            for z in range(self.length):
                self.freqBank[x][z] = self.fundFreq + self.fundFreq * abs(self.length * 0.5 - x) + abs(self.length * 0.5 - z)
                
                self.posInst_freqBank[x][z] = self.freqBank[x][z] * math.pow(2, self.posInst_octave)
                self.velInst_freqBank[x][z] = self.freqBank[x][z] * math.pow(2, self.velInst_octave)
                self.fm_freqBank[x][z] = self.freqBank[x][z] * math.pow(2, self.fm_octave)

    def UpdateNotes(self, status, data1, data2):
        
        print status, data1, data2




    def out(self):
        self.output = Freeverb(input=Clip(self.fm + self.velInst, -1, 1), size=0.5, damp=0.3, bal=0.75)
        self.output.out()
        return self

    """def Debug(self):
        if self.debug == True:
            for x in range(self.length):
                for z in range(self.length):
                    print "Block {0}, {1}: (x = {2}, y = {3}, z = {4})".format(x, z, 
                    self.blocks[x][z].position.x, 
                    self.blocks[x][z].position.y, 
                    self.blocks[x][z].position.z)"""
        
        
