from pyo import *
from Synth_01 import *

class SynthManager:
    def __init__(self, length):
        self.length = length
        

        self.synth1 = FMSynth(length=self.length, octave=0)
        self.synth2 = WTSynth(length=self.length, octave=-1)
        self.synths = [self.synth1, self.synth2]

        #all frequencies from which to choose, will be filled when we play notes
        #self.freqBank = [0]
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
             
            #give the notes to the synths that need them
            self.synth1.UpdateNotes(self.blockNotes)

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
            self.synth2.UpdateNotes(self.notes)
            self.UpdateLayout()
            

        if status == 128: #note off
            self.noteOns.remove(data1)
        if not self.noteOns: #if no more note ons, clear the list at the next note
            self.clearNotes = True #the notes will be cleared next time we have a note on 

            
        ####################################################
        
    def UpdateBlocks(self, blocks):
        #self.synth1.UpdateBlocks(blocks)
        for i in range(len(self.synths)):
            self.synths[i].UpdateBlocks(blocks)
