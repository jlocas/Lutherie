from pyo import *

class SynthData:
    def __init__(self, length, synths):
        self.length = length

        #all frequencies from which to choose, will be filled when we play notes
        self.freqBank = []
        #which index from the freqBank for the block
        self.blockIndex = [[0 for x in range(self.length)] for z in range(self.length)]
        #the frequency itself, the value that is sent to the synth's SigTo. For each individual block
        self.blockFreqs = [[0 for x in range(self.length)] for z in range(self.length)]
        
        self.midi = RawMidi(self.UpdateNotes)
        self.notes = []
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
        
        if self.freqBank:
            if self.layout == "hor":
                for x in range(self.length):
                    for z in range(self.length):
                        self.blockIndex[x][z] = int(float(x) / self.length * len(self.freqBank))
            elif self.layout == "ver":
                 for x in range(self.length):
                    for z in range(self.length):
                        self.blockIndex[x][z] = int(float(z) / self.length * len(self.freqBank))
            elif self.layout == "rad":
                 for x in range(self.length):
                    for z in range(self.length):
                        self.blockIndex[x][z] = int(len(self.freqBank) * (abs(self.length * 0.5 - x) / self.length + abs(self.length * 0.5 - z) / self.length))  
                        
        self.ApplyLayout() 
    
    #to send to blocks
    def ApplyLayout(self):
        for x in range(self.length):
            for z in range(self.length):
                self.blockFreqs[x][z] = self.freqBank[self.blockIndex[x][z]]         
                
        for i in range(synths):
            synths[i].UpdateFreqs(self.blockFreqs)

    def SetLayout(self, layout):
        self.layout = layout
        UpdateLayout()

    def UpdateNotes(self, status, data1, data2):
        #Add notes to a list of notes. 
        #Replace these when new notes are played
        if status == 144: #note on
            self.noteOns.append(data1)
            print data1

            if self.clearNotes:
                self.notes = []
                self.freqBank = []
                self.clearNotes = False
                                
            self.notes.append(data1)
            self.notes.sort()               
            self.freqBank.append(midiToHz(data1))
            self.freqBank.sort()
            
            self.UpdateLayout()
            

        if status == 128: #note off
            self.noteOns.remove(data1)
        if not self.noteOns: #if no more note ons, clear the list at the next note
            self.clearNotes = True #the notes will be cleared next time we have a note on 
            print self.blockIndex

            
        ####################################################
