from pyo import *
from SpringGridBlock import *
#from OSC_Synth import *
from Synth_01 import *
from Controller import *
from SynthManager import *
import sys

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1)
s.setMidiInputDevice(1)
s.boot().start()

#gridLength = int(sys.argv[1])
gridLength = 8
blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]

con = Controller(config=0)
con.debug = False

synman = SynthManager(length=gridLength, blocks=blocks)

#receive OSC for cube sections and how to handle synths
def OSC(address, *args):

    if address == '/springGrid/blockGroups/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].setPosition(args[i * 3], args[i * 3 + 1], args[i * 3 + 2])
                i+=1

        if synman != None:
            synman.UpdateBlocks(blocks)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)

s.gui(locals())
