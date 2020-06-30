from math import *


class Polar():

    def at(self, ratio):
        t = pi * 2 * ratio
        r = self.polar(t)
        x = r * sin(t)
        y = r * cos(t)
        return(x, y)
