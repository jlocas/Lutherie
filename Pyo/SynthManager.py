from pyo import *
from Synth_01 import *


class SynthManager:
    def __init__(self, length, realLength):
        self.length = length
        self.realLength = realLength
        self.size = self.length*self.length
        self.blockHeights = [[0 for x in range(self.length)] for z in range(self.length)]
        
### bus 1 ### 
        self.fmSynth = FMSynth(length=self.length, octave=0, mul=0.5)
        self.wtSynth = WTSynth(length=self.length, octave=-1, mul=0.33)
        
        self.outputs1 = self.fmSynth.GetOutput() + self.wtSynth.GetOutput()
        self.comp = Compress(input = self.outputs1, thresh=-40, ratio=4, risetime=0.1, falltime=0.50, lookahead=0.00, knee=1, outputAmp=False, mul=0.7, add=0)
        self.rvb = Freeverb(input=self.comp, size=0.50, damp=0.50, bal=0.8, mul=1, add=0).out()

### bus 2 ###
        self.pulsynth = Pulsynth2(octave=1, voices=10, spread=5, mul=0.1)
        self.outputs2 = self.pulsynth.GetOutput().out()
        

########FOR BLOCK GROUPS########
        #which index from the freqBank for the block group
        self.blockIndex = [[0 for x in range(self.length)] for z in range(self.length)]
        #the frequency itself, the value that is sent to the synth's SigTo. For each individual block group
        self.blockNotes = [[0 for x in range(self.length)] for z in range(self.length)]
        
########FOR SINGLE BLOCKS########
        self.realBlockIndex = [[0 for x in range(self.realLength)] for z in range(self.realLength)]
        #the frequency itself, the value that is sent to the synth's SigTo. For each individual block
        self.realBlockNotes = [[0 for x in range(self.realLength)] for z in range(self.realLength)]

        
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
            #block groups
            for x in range(self.length):
                for z in range(self.length):
                    # -0.001 parce que la premiere valeur est toujours au dessus du max.
                    #                                                                       v
                    self.blockIndex[x][z] = int((len(self.notes) - 0.00001) * (abs(self.length * 0.5 - x) / self.length + abs(self.length * 0.5 - z) / self.length))  
            #single blocks      
            for x in range(self.realLength):
                for z in range(self.realLength):
                    self.realBlockIndex[x][z] = int((len(self.notes) - 0.00001) * (abs(self.realLength * 0.5 - x) / self.realLength + abs(self.realLength * 0.5 - z) / self.realLength))  

#assign notes to blocks
            #block groups
            for x in range(self.length):
                for z in range(self.length):
                    self.blockNotes[x][z] = self.notes[self.blockIndex[x][z]]         
            #single blocks  
            for x in range(self.realLength):
                for z in range(self.realLength):   
                    self.realBlockNotes[x][z] = self.notes[self.realBlockIndex[x][z]]      

             
            #give the notes to the synths that use blocks for notes
            self.fmSynth.UpdateNotes(self.blockNotes)
            #self.pulsynth.UpdateNotes(self.realBlockNotes)


    def UpdateNotes(self, status, data1, data2):
        #Add notes to a list of notes. 
        #Replace these when new notes are played
        if status == 144: #note on
            self.noteOns.append(data1)

            if self.clearNotes:
                self.notes = []
                self.clearNotes = False
                                
            self.notes.append(data1)
            self.notes.sort()               
            
            #give the notes to the Wave Terrain synth and update the layout to send the notes to the other synths
            self.wtSynth.UpdateNotes(self.notes)
            self.pulsynth.UpdateNotes(self.notes)
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
