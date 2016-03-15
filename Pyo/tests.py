#!/usr/bin/env python
# encoding: utf-8
from pyo import *

s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1).boot()

s.start()

ind = LinTable([(0,100), (200,20), (1000,5), (8191,1)])

size = 20
freqs = 1000

mt = LinTable(list=[(0, 0.0), (10, 1), (6191, 0.0)], size=8192)
mto = Osc(table=mt, freq=1, mul=0.05)

rt = LinTable(list=[(0, 1.0), (8191, 0.0)], size=8192)
rto = Osc(table=rt, freq=1, mul=0.01)

def Tri():
    freqs = [random.triangular(8000, 15000) for i in range(size)]
    f.setCarrier(freqs)


m = Metro(1).play()
tr = TrigEnv(m, table=[ind, mt, rt], dur=0.5)
tf = TrigFunc(input=m, function=Tri, arg=None)

f = CrossFM(carrier=freqs, ratio=rto, ind1=tr, ind2=tr, mul=mto).out()

#rec = Record(input=f, filename="newfile.wav", chnls=2, fileformat=0, sampletype=1, buffering=128)



s.gui(locals())
