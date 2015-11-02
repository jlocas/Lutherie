#!/usr/bin/env python
# encoding: utf-8
from pyo import *
import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def debug(self):
        print " ({0},{1},{2}) ".format(self.x, self.y, self.z)
        
        
    def magnitude(self):
        return math.sqrt((self.x*self.x + self.y*self.y + self.z*self.z))
        

class SpringGridBlock:
    def __init__(self):
        self.position = Vector3(0.0, 0.0, 0.0)
        self.velocity = Vector3(0.0, 0.0, 0.0)
        
    def setPosition(self, x,y,z):
        self.velocity.x = abs(x - self.position.x)
        self.velocity.y = abs(y - self.position.y)
        self.velocity.z = abs(z - self.position.z)
        
        self.position.x = x
        self.position.y = y
        self.position.z = z

