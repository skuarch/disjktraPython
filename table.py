#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:09:09 2019

@author: skuarch
"""

from row import Row

class Table:
    vertexName = ""
    shorttestDistToMain = None
    previusVertex = None
    rows = []
    
    def __init__(self):
        return None

    def addRow(self, row):        
        self.rows.append(row)
        
    def getRows(self):
        return self.rows
    
    def updateRow(self, row):
        index = self.rows.index(row)
        self.rows[index] = row
        
    def getRowByName(self, vertexName):
        for r in self.rows:
            if(r.vertexName == vertexName):
                return r
    