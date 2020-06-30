import math


class CircleGenerator():

    def __init__(self, radius:float, center:(float, float)):
        self.radius = radius
        self.center = center
    
    def at(self, ratio):
        x = self.center[0] + self.radius * math.sin(2 * math.pi * ratio)
        y = self.center[1] + self.radius * math.cos(2 * math.pi * ratio)
        return (x, y)
        
