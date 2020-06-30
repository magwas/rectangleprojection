from math import *
from polar import Polar


class DoubleFolium(Polar):

    def polar(self, t):
        return 4 * cos(t) * (sin(t) ** 2)
