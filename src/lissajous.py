from math import *
from polar import Polar
from trigonometric import Trigonometric


class Lissajous(Trigonometric):

    def __init__(self, n, c):
        self.n = n
        self.c = c

    def trigonometric(self, t):
        x = sin(self.n * t + self.c)
        y = sin(t)
        return (x, y)
