#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SynthData import *
from Synth_01 import *

class SynthManager:
    def __init__(self, length):
        self.length = length
        
        self.synth1 = FMSynth(length=self.length, octave=4)
        self.synths = [self.synth1]
        
        self.syndat = SynthData(length=self.length, synths=self.synths)
    
    def UpdateMidi(self, status, data1, data2):
        #also updates synth notes
        self.syndat.UpdateNotes(status, data1, data2)
        
    def UpdateBlocks(self, blocks):
        self.synth1.UpdateBlocks(blocks)
        #for i in range(len(self.synths)):
            #self.synths[i].UpdateBlocks(blocks)
        