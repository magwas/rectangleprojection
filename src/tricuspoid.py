from math import *

from trigonometric import Trigonometric


class Tricuspoid(Trigonometric):

    def trigonometric(self, t):
        x = 2 * cos(t) + cos(2 * t)
        y = 2 * sin(t) - sin(2 * t)
        return(x, y)
