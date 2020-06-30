from math import *
from polar import Polar


class Sextic(Polar):

    def polar(self, t):
        return 4 * (cos(t / 3) ** 3)

