#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

blocks = [[]] #2d list of SpringGridBlock object
gridLength = 0 #int
groupsPerSide = 0
gridSize = 0

freqs = []
amps = []

def OSC(adress, *args):
    
    global gridLength
    global groupsPerSide
    global gridSize
    global blocks
    
    if adress == '/springGrid/length':
        gridLength = args[0]
        gridSize = gridLength * gridLength
        blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
        print "Grid Length received:", gridLength
        
    if adress == '/springGrid/groupsPerSide':
        groupsPerSide = args[0]
        print "Groups per side:", groupsPerSide
        
    if adress == '/springGrid/blocks/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].position.x = args[i*3]
                blocks[x][z].position.y = args[i*3+1]
                blocks[x][z].position.z = args[i*3+2]
                i += 1

def PrintBlockY():
        for x in range(gridLength):
            for z in range(gridLength):
                    print blocks[x][z].position.y

receiver = OscDataReceive(12543, "/springGrid/*", OSC)


s.gui(locals())
