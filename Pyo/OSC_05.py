#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *
from OSC_Synth import *
import sys

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot().start()

gridLength = int(sys.argv[1])
blocks = [[SpringGridBlock() for x in range(gridLength)] for z in range(gridLength)]
syn = SpringGridSynth(length=gridLength)


def OSC(address, *args):
        
    if address == '/springGrid/blockGroups/positions':
        i = 0
        for x in range(gridLength):
            for z in range(gridLength):
                blocks[x][z].setPosition(args[i * 3], args[i * 3 + 1], args[i * 3 + 2])
                i+=1

        ### "syn" ici, c'est l'objet SpringGridSynth() cree a la ligne 24 (et qui ecrase celui de la ligne 12).
        if syn != None:
            syn.Update(blocks)
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC)

### "syn" ici, c'est l'objet SpringGridSynth() cree a la ligne 12.
### En gros, tu ecoutes un objet qui n'est jamais mis a jour...
#output = Freeverb(input=Clip(syn.getOutput(), -1, 1, 1, 0), size=0.5, damp=0.3, bal=0.75, mul=1, add=0)
#output.out()

### Essais avec ca...
#dummy = Sig(0)
#dummy.out()
#output = Freeverb(input=Clip(dummy, -1, 1), size=0.5, damp=0.3, bal=0.75).out()



s.gui(locals())
