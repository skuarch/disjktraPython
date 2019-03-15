#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:46:25 2019

@author: skuarch
"""

from vertex import Vertex
from table import Table
import math
from row import Row

class Main:
    def __init__(self):
        aVertex = Vertex("a", 0)
        bVertex = Vertex("b", 6)
        cVertex = Vertex("c", 5)
        dVertex = Vertex("d", 1)
        eVertex = Vertex("e", 2)  
        
        visited = []
        unvisited = [aVertex, bVertex, cVertex, dVertex, eVertex]
        allVertex = [aVertex, bVertex, cVertex, dVertex, eVertex]
        
        aVertex.knownVertexes = [bVertex, dVertex]
        bVertex.knownVertexes = [aVertex, cVertex, dVertex, eVertex]
        cVertex.knownVertexes = [bVertex, eVertex]
        dVertex.knownVertexes = [aVertex, bVertex, eVertex]
        eVertex.knownVertexes = [dVertex, bVertex, cVertex]
        
        table = Table()
        aRow = Row("a", 0, None)
        bRow = Row("b", math.inf, None)
        cRow = Row("c", math.inf, None)
        dRow = Row("d", math.inf, None)
        eRow = Row("e", math.inf, None)
        
        table.addRow(aRow)
        table.addRow(bRow)
        table.addRow(cRow)
        table.addRow(dRow)
        table.addRow(eRow)
        
        for vertex in allVertex:                       
            for knownVertex in vertex.knownVertexes:                
                s = vertex.distance + knownVertex.distance
                row = table.getRowByName(knownVertex.name)
                if s < row.shorttestDistToMain:
                    row.shorttestDistToMain = s
                    row.previousVertex = vertex.name
                    table.updateRow(row)
        
        rows = table.getRows()
        for r in rows:
            print("name {} short {} previous {}".format(r.vertexName, r.shorttestDistToMain, r.previousVertex))
    
    def getShorttesVertexUnvisited(self, vertex):
        m = min(vertex.knownVertexes)
        for u in allVertex:
            if u == m:
                return m        
        
Main()

