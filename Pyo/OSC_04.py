#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

"""receive blocks as groups"""

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
       SetupSynth()

    if adress == '/springGrid/blockGroups/positions':
        UpdateSynth(args)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)


def SetupSynth():
    global freqs
    global instr
    global amps
    
    fundFreq = 50
    #freqs = [SigTo(value=100, time=0.1, init=100) for i in range(gridSize)]
    freqs = [0 for i in range(gridSize)]
    amps = [SigTo(value=0, time=0.1, init=0) for i in range(gridSize)]
    i=0
    
    for x in range(gridLength):
        for z in range(gridLength):
            #freqs[i].setValue(fundFreq + fundFreq * (x + z))
            freqs[i] = fundFreq + fundFreq * (x + z)
            i += 1
            
    instr = SumOsc(freq = freqs, ratio=1, index=0.5, mul=amps).out()
    
def UpdateSynth(args):
    global amps
    global freqs
    
    i = 0
    
    for x in range(gridLength):
        for z in range(gridLength):
            amps[i].setValue( args[i * 3 + 1] * 0.1 )
            #freqs[i].setValue( freqs[i] + freqs[i] * args[i*3] + args[i*3+2] )
            freqs[i] = freqs[i] + freqs[i] * args[i*3] + args[i*3+2]
            i+=1
    
    instr.setMul(amps)
    #instr.setFreq(freqs)
    
instr.out()



s.gui(locals())
