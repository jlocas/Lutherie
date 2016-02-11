#!/usr/bin/env python
# encoding: utf-8
from pyo import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

#receive OSC for cube sections and how to handle synths
def OSC(address, *args):
    if address == '/springGrid/blockGroups/positions':
        print "receive!"
        print args
            
        
receiver = OscDataReceive(12543, "/springGrid/*", OSC) 

sender = OscDataSend("iiiiiiiii", 12543, "/springGrid/blockGroups/positions")
msg = [0,0,0,1,0,0,1,0,1]

#sender.send(msg)


s.gui(locals())
