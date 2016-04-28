# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:41:00 2016

@author: tzupan
"""

import pandas as pd
import numpy as np

def findneighbors(mylist):
    '''
    '''  
    northNeighbor = None
    westNeighbor = None
    southNeighbor = None
    eastNeighbor = None
    
    listOfCoords = np.asarray(mylist)
    
    for point in listOfCoords:
        allPossibleNeighbors = point - listOfCoords
