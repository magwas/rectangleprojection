#!/usr/bin/python3
import math


class RectangleProjection():

    def height(self, a:(float, float), b:(float, float)):
        return math.sqrt(
            (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        )
    
    def middle(self, a:(float, float), b:(float, float)):
        return (
            (a[0] + b[0]) / 2 , (a[1] + b[1]) / 2
        )

    def ProjectPair(self, p1, p2):
        x, y = self.middle(p1, p2)
        z = self.height(p1, p2)
        return (x, y, z)

    def project(self, ps):
        ret = []
        l = len(ps)
        for i in range(l):
            row = []
            for j in range(l):
                p1 = ps[i % l]
                p2 = ps[j % l]
                row.append(self.ProjectPair(p1, p2))
            ret.append(row)
        return ret
