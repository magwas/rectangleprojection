from math import *
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
from projection import RectangleProjection


class Animator():

    def __init__(self, generator, numpoints=50):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.generator = generator
        self.numpoints = numpoints
    
    def generate(self):
        print('generating...\n')
        generator = self.generator
        projection = RectangleProjection()
        
        numpoints = self.numpoints
        points = []
        for point in range(numpoints):
            points.append(generator.at(point / numpoints))
        
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], zs=[0, 0], color='green')
            
        for row in projection.project(points):
            l = len(row)
            for i in range(l):
                p1 = row[i]
                p2 = row[(i + 1) % l]
                self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], zs=[p1[2], p2[2]], color='black')
        print('done...\n')
        return self.fig,
    
    def animate(self, i):
        self.ax.view_init(elev=10., azim=i)
        print('\r%s ' % i, end="")
        return self.fig,

    def __call__(self, filename='animation.mp4'):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.generate,
                                       frames=100, interval=20, blit=True)
        anim.save(filename, fps=30, extra_args=['-vcodec', 'libx264'])
