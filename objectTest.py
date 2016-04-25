# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:44:33 2016

@author: tzupan
"""

import island_class as i
import unittest
reload(i)

class objectTest(unittest.TestCase):
    def test_ObjectType(self):
        practiceIsland = i.island((5,3), 12)
        self.assertTrue(practiceIsland, object)
        