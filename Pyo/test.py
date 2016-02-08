#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SynthHub import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()
s.setMidiInputDevice(1)
s.start()

fb = [5, 9, 10]
l = 8
ll = l/l
for x in range(l):
    for z in range(l):
        #print (x * ll)
        pass

sh = SynthHub(l)


s.gui(locals())
