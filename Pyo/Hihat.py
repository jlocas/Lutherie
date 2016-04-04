from pyo import *

class Hihat:
    def __init__(self):

        self.hattab = SndTable(path=['samples/SHD_808HH_01.wav', 'samples/SHD_808OH_01.wav'])
        self.hatptr = TableRead(table=self.hattab, freq=self.hattab.getRate(), loop=0, interp=2, mul=1, add=0)
        self.hatpat = [0,0,0,1]
        
        self.snartab = SndTable(path='samples/snare.wav')
        self.snarptr = TableRead(table=self.snartab, freq=self.snartab.getRate(), loop=0, interp=2, mul=1, add=0)
        self.snarpat = [0,1,0,1]
        
        self.kicktab = SndTable(path='samples/kick.wav')
        self.kickptr = TableRead(table=self.kicktab, freq=self.kicktab.getRate(), loop=0, interp=2, mul=1, add=0)
        self.kickpat = [1,0,0,0]
        
        
        self.ind = 0
                                                    
    def Trigg(self):
        self.hatptr[self.hatpat[self.ind]].out()
        
        
        if self.snarpat[self.ind] == 1:
            self.snarptr.out()
            
        if self.kickpat[self.ind] == 1:
            self.kickptr.out()

        self.ind = (self.ind + 1) % 4

    def GetOutput(self):
        return self.output
