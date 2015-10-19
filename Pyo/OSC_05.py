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
ffreqs = []
amps = []

instr = Sine(freq = 100, mul=0.1)


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
    global ffreqs

    fundFreq = 40
    freqs = [SigTo(value=100, time=0.1, init=100) for i in range(gridSize)]
    ffreqs = [0 for i in range(gridSize)]
    amps = [SigTo(value=0, time=0.1, init=0) for i in range(gridSize)]
    i=0
    
    for x in range(gridLength):
        for z in range(gridLength):
            freqs[i].setValue(fundFreq + fundFreq * (x + z))
            ffreqs[i] = fundFreq + fundFreq * (x + z)
            i += 1
            
    instr = Sine(freq = freqs, mul=amps).out()
    
def UpdateSynth(args):
    global amps
    global freqs
    global ffreqs

    i = 0
    
    for x in range(gridLength):
        for z in range(gridLength):
            amps[i].setValue( args[i * 3 + 1] * 0.1 )
            freqs[i].setValue( ffreqs[i] + ffreqs[i] *(args[i*3] + args[i*3+2]) * 0.001 )
            #freqs[i] = freqs[i] + freqs[i] * args[i*3] + args[i*3+2]
            i+=1
    
    instr.setMul(amps)
    instr.setFreq(freqs)
    
output = Freeverb(input=Clip(instr, -1, 1, 1, 0), size=0.5, damp=0.3, bal=0.75, mul=1, add=0)
output.out()



s.gui(locals())
