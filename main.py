#!/usr/bin/python3
from math import *
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

from animator import Animator
from cardioid import Cardioid
from circlegenerator import CircleGenerator
from doublefolium import DoubleFolium
from figureeigth import FigureEight
from lissajous import Lissajous
import matplotlib.pyplot as plt
from nephroid import Nephroid
from polar import Polar
from projection import RectangleProjection
from rhodonea import Rhodonea
from sextic import Sextic
from tricuspoid import Tricuspoid
from trifolium import Trifolium

numpoints = 100     
Animator(DoubleFolium(), numpoints)('doublefolium.mp4')
Animator(Sextic(), numpoints)('sextic.mp4')
Animator(Lissajous(3, 2), numpoints)('lissajous.mp4')
Animator(Trifolium(), numpoints)('trifolium.mp4')
Animator(Tricuspoid(), numpoints)('tricuspoid.mp4')
Animator(Cardioid(), numpoints)('cardioid.mp4')
Animator(Nephroid(), numpoints)('nephroid.mp4')
Animator(Rhodonea(5), numpoints)('rhodonea5.mp4')
Animator(Rhodonea(3), numpoints)('rhodonea3.mp4')
Animator(Rhodonea(5), numpoints)('rhodonea6.mp4')
Animator(FigureEight(), numpoints)('figure8.mp4')

