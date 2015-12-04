from pyo import *
from SpringGridBlock import *
from OSC_Synth import *
from Controller import *
import sys

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1)
s.setMidiInputDevice(99)
s.boot().start()

gridLength = int(sys.argv[1])
#gridLength = 8
blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
syn = SpringGridSynth(length=gridLength)

con = Controller(config=0)
con.debug = False

#receive OSC for cube sections and how to handle synths
def OSC(address, *args):
        
    if address == '/springGrid/blockGroups/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].setPosition(args[i * 3], args[i * 3 + 1], args[i * 3 + 2])
                i+=1

        if syn != None:
            syn.Update(blocks)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)

s.gui(locals())
