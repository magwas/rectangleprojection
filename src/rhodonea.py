from math import *
from polar import Polar


class Rhodonea(Polar):

    def __init__(self, k):
        self.k = k

    def polar(self, t):
        return sin(self.k * t)
