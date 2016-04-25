# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:44:40 2016

@author: tzupan
"""

class island(object):
    '''
    '''
    def __init__(self, location, bridgesIn):
        self.location = location
        self.degree = 0
        self.bridgesIn = bridgesIn
        self.neighbors = {}
        
    def addNeighbor(self, neighbor):
        '''
        neighbor will be passed as a tuple of (name, neighborLocation)
        '''
        self.neighbors[neighbor[0]] = neighbor[1]
        
    