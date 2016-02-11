#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SynthData import *
from Synth_01 import *

class SynthManager:
    def __init__(self, length, blocks):
        self.length = length
        self.blocks = blocks
        
        self.synth1 = FMSynth(length=self.length)
        self.s = FM()
        self.syndat = SynthData(length=self.length, synths=[self.s])
    
    def UpdateMidi(self, status, data1, data2):
        self.syndat.UpdateNotes(status, data1, data2)
        
    def UpdateBlocks(self, blocks):
        self.blocks = blocks