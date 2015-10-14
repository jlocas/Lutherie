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
filters = []

src = PinkNoise(mul=1).play()


def OSC(adress, *args):
    
    global gridLength
    global gridSize
    global blocks

    if adress == '/springGrid/length':
       gridLength = args[0]
       gridSize = gridLength*gridLength
       blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
       SetupFilters()

    if adress == '/springGrid/blocks/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                #3 valeurs par block dans la liste 
                blocks[x][z].position.x = args[i * 3]
                blocks[x][z].position.y = args[i * 3 + 1]
                blocks[x][z].position.z = args[i * 3 + 2]

                i+=1
                
        UpdateFilters(args)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)


def SetupFilters():
    global freqs
    global src
    global amps
    global filters
    
    fundFreq = 50
    freqJump = 2
    freqs = [0 for i in range(gridSize)]
    amps = [0 for i in range(gridSize)]
    filters = [Biquad(input=src, freq=100, q=100, type=2, mul=0.5) for i in range (gridSize)]


    i=0
    
    for x in range(gridLength):
        for z in range(gridLength):
            freqs[i] = fundFreq + fundFreq * (x + z)
            filters[i].out()
            i += 1
            
    
def UpdateFilters(args):
    global amps
    global freqs
    
    i = 0
    
    for x in range(gridLength):
        for z in range(gridLength):
            amps[i] = args[i * 3+1]
            freqs[i] = freqs[i] + args[i * 3] + args[i * 3+2]
            filters[i].setFreq(freqs[i])
            filters[i].setMul(amps[i])

            i+=1
            
    print freqs
    




s.gui(locals())
