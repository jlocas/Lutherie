from pyo import *
from Synth_01 import *
from Synth_02 import *
from Pulsynth import *

class SynthManager:
    def __init__(self, length, realLength):
        self.length = length
        self.realLength = realLength
        self.size = self.length*self.length
        
        self.blockHeights = [[0.0 for x in range(self.length)] for z in range(self.length)]
        self.blockSpeeds = [[0.0 for x in range(self.length)] for z in range(self.length)]
        self.avgSpeed = 0.0
        self.avgHeight = 0.0
        self.avgDev = 0.0
        
### bus 1 ### 
        self.fmSynth = FMSynth(length=self.length, octave=-1, mul=0.1)
        self.wtSynth = WTSynth(length=self.length, octave=0, mul=0.007)
        self.velSynth = VelSynth(length=self.length, octave=3, mul=0.1)
        self.velSynth2 = VelSynth2(octave=8, voices=10, mul=0.005)       

        
        self.outputs1 = Mix(input=self.fmSynth.GetOutput() + self.wtSynth.GetOutput() + self.velSynth.GetOutput() + self.velSynth2.GetOutput(), voices=2, mul=1, add=0)
        #self.outputs1 = Mix(input=self.wtSynth.GetOutput(), voices=2, mul=1, add=0)
        #self.outputs1 = Mix(input=self.fmSynth.GetOutput(), voices=2, mul=1, add=0)
        #self.outputs1 = Mix(input=self.velSynth2.GetOutput(), voices=2, mul=1, add=0)

        self.comp1a = Compress(input=self.outputs1, thresh=-20, ratio=12, risetime=0.1, falltime=0.5, lookahead=0.00, knee=1, outputAmp=False, mul=1, add=0)
        self.lim1a = Compress(input=self.comp1a, thresh=-0.1, ratio=100, risetime=0.001, falltime=0.002, lookahead=5.00, knee=0, outputAmp=False, mul=1, add=0)
        
### bus 2 ###
        self.pulsynth = Pulsynth(octave=5, voices=10, spread=2, mul=0.015)
        self.outputs2 = self.pulsynth.GetOutput()

### bus 3 ###
        self.choir = Choir(mul=0.35)
        self.outputs3 = self.choir.GetOutput()

###master###
        self.masterbus = DCBlock(self.lim1a + self.outputs2 + self.outputs3)
        #self.mastrvb = Freeverb(input=self.masterbus, size=0.50, damp=0.80, bal=0.5, mul=1, add=0).out()
        self.mastcomp1 = Compress(input=self.masterbus, thresh=-30, ratio=1.1, risetime=0.5, falltime=1, lookahead=0.00, knee=1, outputAmp=False, mul=2, add=0)
        self.mastcomp2 = Compress(input=self.mastcomp1, thresh=-15, ratio=5, risetime=0.01, falltime=0.02, lookahead=0.00, knee=1, outputAmp=False, mul=2, add=0)
        self.mastcomp3 = Compress(input=self.mastcomp2, thresh=-5, ratio=15, risetime=0.01, falltime=0.02, lookahead=0.00, knee=1, outputAmp=False, mul=1, add=0)
        self.mastlim = Compress(input=self.mastcomp3, thresh=-0.1, ratio=100, risetime=0.001, falltime=0.002, lookahead=0.00, knee=1, outputAmp=False, mul=1, add=0)
        self.mastclip = Clip(input=self.mastlim, min=-1.00, max=1.00, mul=1, add=0).out()



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
            self.velSynth.UpdateNotes(self.blockNotes)


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
            self.velSynth2.UpdateNotes(self.notes)

            self.UpdateLayout()
            

        if status == 128: #note off
            self.noteOns.remove(data1)
        if not self.noteOns: #if no more note ons, clear the list at the next note
            self.clearNotes = True #the notes will be cleared next time we have a note on 

            
        ####################################################
        
    def UpdateBlockHeights(self, heights):

        for x in range(self.length):
            for z in range(self.length):
                self.blockHeights[x][z] = heights[x][z]
                        
        self.fmSynth.UpdateHeights(self.blockHeights)
        self.wtSynth.UpdateHeights(self.blockHeights)

    def UpdateBlockSpeeds(self, speeds):
        self.i = 0
        for x in range(self.length):
            for z in range(self.length):
                self.blockSpeeds[x][z] = speeds[self.i]
                self.i += 1
                
        self.velSynth.UpdateSpeeds(speeds)
                
    def UpdateAverageHeight(self, avgy):
        self.fmSynth.UpdateAverageHeight(avgy)
        self.velSynth.UpdateAverageHeight(avgy)
        

    def UpdateAverageHeightDev(self, avgydev):
        self.fmSynth.UpdateAverageHeightDev(avgydev)
        self.wtSynth.UpdateAverageHeightDev(avgydev)
        self.velSynth.UpdateAverageHeightDev(avgydev)
        self.velSynth2.UpdateAverageHeightDev(avgydev)
        self.choir.UpdateAverageHeightDev(avgydev)
        

    def UpdateAverageDeviation(self, avgdev):
        self.fmSynth.UpdateAverageDeviation(avgdev)
        self.wtSynth.UpdateAverageDeviation(avgdev)
        self.velSynth.UpdateAverageDeviation(avgdev)
        self.velSynth2.UpdateAverageDeviation(avgdev)
        self.choir.UpdateAverageDeviation(avgdev)

        
    def UpdateAverageVelocity(self, avgvel):
        self.wtSynth.UpdateAverageVelocity(avgvel)
        self.velSynth2.UpdateAverageVelocity(avgvel)
        
