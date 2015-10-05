#!/usr/bin/env python
# encoding: utf-8
from pyo import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

size = 5
freqs = [0 for i in range(size)]
amps = [0.3 for i in range(size)]

for i in range(size):
    freqs[i] = 50 + 50 * i
    

src = PinkNoise()
filters = Biquad(input = src, freq = freqs, q = 10, mul = amps).out()


s.gui(locals())
