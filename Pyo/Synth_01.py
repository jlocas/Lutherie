#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *
import math

class SpringGridSynth:
    def __init__(self, length=8):
        
        self.length = length
        self.size = self.length*self.length
    
        self.freqBank = [[0 for x in range(self.length)] for z in range(self.length)]
        self.midi = RawMidi(self.UpdateNotes)
        
        
        #each square of the grid has its own freq and amplitude
        self.freqs = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)] #list of SigTo's
        self.amps = [SigTo(value=0.0, time=0.1, init=0) for i in range(self.size)]

        self.notes = []
        self.noteFreqs = []
        self.noteOns = []
        self.clearNotes = True #to immediately add new notes to the list

        self.debug = False
        
        self.out()
        
    #receive data from blocks / block groups and apply them to the synth
    def Update(self, blocks):
        self.blocks = blocks

        i = 0
        for x in range(self.length):
            for z in range(self.length):      
                pass          
    
        self.Debug()
                

    def UpdateNotes(self, status, data1, data2):
        
        #Add notes to a list of notes. 
        #Replace these when new notes are played
        if status == 145: #note on
            self.noteOns.append(data1)

            if self.clearNotes:
                self.notes = []
                self.clearNotes = False
                                
            self.notes.append(data1)
            self.notes.sort()
            

        if status == 129: #note off
            self.noteOns.remove(data1)
        if not self.noteOns: #no note ons
            self.clearNotes = True #the notes will be cleared next time we have a note on 
            
        ####################################################

        self.blocksPerNote = self.size / self.notes.length()
            
            
    def FillFreqs(self):
        

    def out(self):

        return self

    def Debug(self):
        if self.debug == True:
            for x in range(self.length):
                for z in range(self.length):
                    print "Block {0}, {1}: (x = {2}, y = {3}, z = {4})".format(x, z, 
                    self.blocks[x][z].position.x, 
                    self.blocks[x][z].position.y, 
                    self.blocks[x][z].position.z)
        
        
