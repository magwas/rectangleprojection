from math import *
from polar import Polar


class FigureEight(Polar):

    def polar(self, t):
        return sqrt(abs(cos(2 * t) * ((1 / cos(t)) ** 4)))
