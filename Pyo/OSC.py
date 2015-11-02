#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

blocks = [[]] #2d list of SpringGridBlock object
gridLength = 0 #int
gridSize = 0

freqs = []
amps = []

instr = SumOsc(freq = 100, ratio=0.2, index=0.2, mul=0.1)


def OSC(adress, *args):
    
    global gridLength
    global gridSize
    global blocks

    if adress == '/springGrid/groupsPerSide':
       gridLength = args[0]
       gridSize = gridLength*gridLength
       blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
       SetupSynth()

    if adress == '/springGrid/blockGroups/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].position.x = args[i * 3]
                blocks[x][z].position.y = args[i * 3 + 1]
                blocks[x][z].position.z = args[i * 3 + 2]
                i+=1
                
        UpdateSynth()
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)


def SetupSynth():
    global freqs
    global instr
    global amps
    
    fundFreq = 50
    freqs = [0 for i in range(gridSize)]
    amps = [0 for i in range(gridSize)]
    i=0
    
    for x in range(gridLength):
        for z in range(gridLength):
            freqs[i] = fundFreq + fundFreq * (x + z)
            i += 1
            
    instr = SumOsc(freq = freqs, ratio=1, index=0.5, mul=amps).out()
    
def UpdateSynth():
    global amps
    global freqs
    
    i = 0
    
    for x in range(gridLength):
        for z in range(gridLength):
            amps[i] = blocks[x][z].position.y * 0.1
            #freqs[i] = freqs[i] + freqs[i] * blocks[x][z].position.x + blocks[x][z].position.z
            i+=1
    
    instr.setMul(amps)
    
instr.out()



s.gui(locals())
