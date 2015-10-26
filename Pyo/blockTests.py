#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()


block = SpringGridBlock()

instr = Sine(100, 0, 1)
dummy = Sig(0)
dummy.value = instr
dummy.out()

s.gui(locals())
