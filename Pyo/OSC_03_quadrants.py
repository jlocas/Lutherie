#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

gridLength = 0
fm = FM(carrier = 100, ratio = 2, index = 0, mul=0.1)
fmlist = []

def OSC(adress, *args):
    
    global gridLength
    global gridSize
    global blocks

    if adress == '/springGrid/groupsPerSide':
        gridLength = args[0]
        fmlist = [fm for i in range(gridLength)]
        
    if adress == '/springGrid/blockGroups/positions':
        
        

receiver = OscDataReceive(12543, "/springGrid/*", OSC)
            
    
    




s.gui(locals())
