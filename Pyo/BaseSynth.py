from pyo import *
from SpringGridBlock import *

class BaseInst:
    def __init__(self, length, octave):
        self.length = length
        self.octave = octave
        
        self.notes = []
        self.amps = [[SigTo(value=0, time=0.02, init=100) for x in range(self.length)] for z in range(self.length)]
        

    def UpdateBlocks(self, blocks):
        for x in range(self.length):
            for z in range(self.length):
                self.amps[x][z].setValue(blocks[x][z].position.y * 0.1)
                
        self.src.setMul(self.amps)


s.gui(locals())
