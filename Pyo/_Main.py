from pyo import *
from SpringGridBlock import *
from Synth_01 import *
from Controller import *
from SynthManager import *
import sys

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1)
s.setMidiInputDevice(3)
s.boot().start()


if len(sys.argv) > 1:
    gridLength = int(sys.argv[1])
else: 
    gridLength = 8

blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]

con = Controller(config=0)
con.debug = False

synman = SynthManager(length=gridLength)

#receive OSC for cube sections and how to handle synths
def OSC(address, *args):
    if address == '/springGrid/blockGroups/positions':
        print "receive!"
        print args
        """i = 0
        
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].setPosition(args[i * 3], args[i * 3 + 1], args[i * 3 + 2])
                i+=1

        if synman != None:
            synman.UpdateBlocks(blocks)"""
            
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC) 

sender = OscDataSend("iiiiiiiii", 12543, "/springGrid/blockGroups/positions")
msg = [0,0,0,1,0,0,1,0,1]

#sender.send(msg)

s.gui(locals())
