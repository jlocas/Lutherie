#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from SpringGridBlock import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

s.start()
size = 10
snd = SndTable("audio_02.wav")
env = HannTable()
pos = [random.randrange(snd.getSize(0)) for i in range(size)]
dur = [Noise(.001, .1) for i in range(size)]
pit = [1, 1.001, 0.999]
g = Granulator(snd, env, pit, pos, dur, 24, mul=.1).out()

s.gui(locals())
