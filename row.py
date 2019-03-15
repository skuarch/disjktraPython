#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:19:41 2019

@author: skuarch
"""

class Row:
    vertexName = ""
    shorttestDistToMain = None
    previousVertex = None
    def __init__(self, vertexName, shorttestDistToMain, previousVertex):
        self.vertexName = vertexName
        self.shorttestDistToMain = shorttestDistToMain
        self.previousVertex = previousVertex
        