from pyo import *
from Synth_01 import *


class SynthManager:
    def __init__(self, length):
        self.length = length
        self.size = self.length*self.length
        self.blockHeights = [[0 for x in range(self.length)] for z in range(self.length)]
        

        self.fmSynth = FMSynth(length=self.length, octave=-1)
        self.wtSynth = WTSynth(length=self.length, octave=0)
        
        self.outputs1 = self.fmSynth.GetOutput() + self.wtSynth.GetOutput()
        self.comp = Compress(input = self.outputs1, thresh=-40, ratio=4, risetime=0.1, falltime=0.50, lookahead=0.00, knee=1, outputAmp=False, mul=0.7, add=0)
        self.rvb = Freeverb(input=self.comp, size=0.50, damp=0.50, bal=0.8, mul=1, add=0).out()

        self.pulsynth = Pulsynth(length=self.length, octave=2)
        self.outputs2 = self.pulsynth.GetOutput().out()

        

        #which index from the freqBank for the block
        self.blockIndex = [[0 for x in range(self.length)] for z in range(self.length)]
        #the frequency itself, the value that is sent to the synth's SigTo. For each individual block
        self.blockNotes = [[0 for x in range(self.length)] for z in range(self.length)]
        
        self.midi = RawMidi(self.UpdateNotes)
        self.notes = [0, 4, 7]
        self.noteFreqs = []
        self.noteOns = []
        self.clearNotes = True #to immediately add new notes to the 
        

        """
        how block indices will be attributed

        layouts:
            hor: horizontal
            ver: vertical
            rad: radial
        
        directions:
            inc: increasing
            dec: decreasing
            
        """
        self.layout = "rad"
        self.dir = "inc"

        self.UpdateLayout()
        

    def UpdateLayout(self):
        
        if self.notes:
            if self.layout == "hor":
                for x in range(self.length):
                    for z in range(self.length):
                        self.blockIndex[x][z] = int(float(x) / self.length * len(self.notes))
            elif self.layout == "ver":
                 for x in range(self.length):
                    for z in range(self.length):
                        self.blockIndex[x][z] = int(float(z) / self.length * len(self.notes))
            elif self.layout == "rad":
                 for x in range(self.length):
                    for z in range(self.length):
                        # -0.001 parce que la premiere valeur est toujours au dessus du max.
                        #                                                                       v
                        self.blockIndex[x][z] = int((len(self.notes) - 0.00001) * (abs(self.length * 0.5 - x) / self.length + abs(self.length * 0.5 - z) / self.length))  
                        
            for x in range(self.length):
                for z in range(self.length):
                    #assign notes to blocks
                    self.blockNotes[x][z] = self.notes[self.blockIndex[x][z]]         
             
            #give the notes to the synths that use blocks for notes
            self.fmSynth.UpdateNotes(self.blockNotes)
            self.pulsynth.UpdateNotes(self.blockNotes)


    def UpdateNotes(self, status, data1, data2):
        #Add notes to a list of notes. 
        #Replace these when new notes are played
        if status == 144: #note on
            self.noteOns.append(data1)
            #print data1

            if self.clearNotes:
                self.notes = []
                self.clearNotes = False
                                
            self.notes.append(data1)
            self.notes.sort()               
            
            #give the notes to the Wave Terrain synth and update the layout to send the notes to the other synths
            self.wtSynth.UpdateNotes(self.notes)
            self.UpdateLayout()
            

        if status == 128: #note off
            self.noteOns.remove(data1)
        if not self.noteOns: #if no more note ons, clear the list at the next note
            self.clearNotes = True #the notes will be cleared next time we have a note on 

            
        ####################################################
        
    def UpdateBlocks(self, blocks):

        for x in range(self.length):
            for z in range(self.length):
                self.blockHeights[x][z] = blocks[x][z].position.y
                
        self.avgheight = self.AverageAbs(self.blockHeights)
        
        self.fmSynth.UpdateHeights(self.blockHeights, self.avgheight)
        self.wtSynth.UpdateHeights(self.blockHeights)
        
            
    def AverageAbs(self, l):
        self.sum = 0

        for x in range(self.length):
            for z in range(self.length):
                self.sum += abs(l[x][z])
            
        return self.sum / self.size
