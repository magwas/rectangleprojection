from math import *


class Nephroid():

    def at(self, ratio):
        t = pi * 2 * ratio + 0.00000001
        x = 3 * cos(t) - cos(3 * t)
        y = 3 * sin(t) - sin(3 * t)
        return(x, y)
