from pyo import *
from SpringGridBlock import *
from Synth_01 import *
from Controller import *
from SynthManager import *
import sys

s = Server(sr=44100, nchnls=2, buffersize=4096, duplex=1)
s.setMidiInputDevice(3)
s.boot().start()


if len(sys.argv) > 1:
    gridLength = int(sys.argv[1])
    realGridLength = int(sys.argv[2])
else: 
    gridLength = 4
    realGridLength = 32

blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
heights = [[0.0 for x in range(gridLength)] for z in range(gridLength)]

con = Controller(config=0)
con.debug = False

synman = SynthManager(length=gridLength, realLength=realGridLength)

#receive OSC for cube sections and how to handle synths
def OSC(address, *args):
    if address == '/springGrid/blockGroups/positions':

        i = 0
        
        for x in range(gridLength):
            for z in range(gridLength):
                heights[x][z] = args[i]
                i+=1

        if synman != None:
            synman.UpdateBlockHeights(heights)
            
    if address == '/springGrid/blockGroups/vels':
        synman.UpdateBlockSpeeds(args)
        
    if address == '/springGrid/blockGroups/avgdev':
        synman.UpdateAverageDeviation(args[0])
        
    if address == '/springGrid/blockGroups/avgy':
        synman.UpdateAverageHeight(args[0])
        
    if address == '/springGrid/blockGroups/avgvel':
        synman.UpdateAverageVelocity(args[0])

    if address =='/springGrid/rain2/ballHit':
        synman.pulsynth.Pulse()
        #synman.hat.Trigg()

        
receiver = OscDataReceive(12543, "/springGrid/*", OSC) 

s.gui(locals())
