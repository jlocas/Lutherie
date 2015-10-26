#!/usr/bin/env python
# encoding: utf-8
from pyo import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

scales = {'major' : [0,2,4,5,7,9,11], 'minorM' : [0,2,3,5,7,8,10], 'minorH' : [0,2,3,5,7,8,11], 'penta' : [0,2,5,7,9]}
scale = scales[ 'major' ]
tonic = 0
octave = 2



instr = Sine(freq = )

s.gui(locals())
