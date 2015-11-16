#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *
from OSC_Synth import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

blocks = [[]] #2d list of SpringGridBlock object
gridLength = 0 #int

syn = None ### Seulement une variable globale du genre "place holder"...

def OSCReceive(address, *args):
    
    global gridLength
    global blocks
    global syn

    if address == '/springGrid/groupsPerSide':
        gridLength = args[0]
        blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
        syn = SpringGridSynth(length=gridLength)

    if address == '/springGrid/blockGroups/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].setPosition(args[i * 3], args[i * 3 + 1], args[i * 3 + 2])
                i+=1

        if syn != None:
            syn.Update(blocks)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSCReceive)


s.gui(locals())
