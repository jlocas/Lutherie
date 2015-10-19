#!/usr/bin/env python
# encoding: utf-8
from pyo import *

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class SpringGridBlock:
    def __init__(self):
        self.position = Vector3(0,0,0)
        self.oldPos = Vector3(0,0,0)
        
    def SetPosition(self, pos):
        self.position = pos
        
    def GetPosition(self):
        return self.position
        
    def Update(self, x, y, z):
        return 