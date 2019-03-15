#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:49:03 2019

@author: skuarch
"""

import math

class Vertex:
    
    name = ""
    distance = math.inf
    knownVertexes = []
    
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        
    def addKnownVertex(self, knownVertex):
        self.knownVertexes.append(knownVertex)
    