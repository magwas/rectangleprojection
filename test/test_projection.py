#!/usr/bin/python3

import math
import unittest

from circlegenerator import CircleGenerator
from projection import RectangleProjection


class TestRectangleProjection(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)  
        self.projection = RectangleProjection()

    def test1(self):
        "The projection height for (0,0),(0.0) is zero"
        self.assertEqual(0.0, self.projection.height(
            (0.0, 0.0), (0.0, 0.0))
        )

    def test2(self):
        "The projection height for (1,0),(0.0) is 1"
        self.assertEqual(1, self.projection.height(
            (1.0, 0.0), (0.0, 0.0))
        )

    def test3(self):
        "The projection height for (1,0),(0.1) is sqrt(2)"
        self.assertEqual(math.sqrt(2.0), self.projection.height(
            (1.0, 0.0), (0.0, 1.0))
        )
        
    def test4(self):
        "the middle point is the average of coordinates"
        self.assertEqual((0.5, 0.5), self.projection.middle(
            (1.0, 0.0), (0.0, 1.0))
        )

    def test5(self):
        "the circlegenerator(radius=100,center=(100,100)) gives [(100,200)] for rad=0"
        self.assertEqual((100.0, 200.0),
                         CircleGenerator(100, (100, 100)).at(0.0)
        )
    
    def test6(self):
        "the circlegenerator(radius=100,center=(100,100)) gives [(200,100)] for 0.25"
        self.assertEqual((200.0, 100.0),
                         CircleGenerator(100, (100, 100)).at(0.25)
        )
    
    def test7(self):
        "the projection returns [[(1,0,0),(0.5,0.5,sqrt(2)],[(0.5,0.5,sqrt(2),(0,1,0)]] for [(1,0)],[(0,1)]"
        self.assertEqual(
            [
                [(1, 0, 0), (0.5, 0.5, math.sqrt(2))],
                [(0.5, 0.5, math.sqrt(2)), (0, 1, 0)]
            ],
                         self.projection.project([(1, 0), (0, 1)])
        )

"""
    def test8(self):
        "the projection returns [(0.5,0.5,sqrt(2)),(0] for [(1,0),(0,0)],[(0,1)]"
        self.assertEqual([(0.5, 0.5, math.sqrt(2)), (0, 0.5, 1)],
                         self.projection.project([(1, 0), (0, 0)], [(0, 1)])
        )

    def test8(self):
        "the projection returns [(0.5,0.5,sqrt(2)),(0] for [(1,0),(0,0)],[(0,1)]"
        self.assertEqual([(0.5, 0.5, math.sqrt(2)), (0, 0.5, 1)],
                         self.projection.project([(1, 0), (0, 0)], [(0, 1)])
        )

"""
