from math import *
from polar import Polar


class Trifolium(Polar):

    def polar(self, t):
        return cos(t) * (4 * (sin(t) ** 2) - 1)
