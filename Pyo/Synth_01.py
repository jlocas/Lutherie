#!/usr/bin/env python
# encoding: utf-8
from pyo import *

class OscGrid:
    def __init__(self, freq=100, ratio=0, index=0, mul=0.5):
        self.freq = freq
        self.ratio = ratio
        self.index = index
        self.mul = mul
        
    def SetFreq(x):
        self.freq = x
        
    def SetRatio(x):
        self.ratio = x
        
    def SetIndex(x):
        self.index = x
        
    def SetMul(x):
        self.mul = x