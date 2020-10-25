import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from algorithms import *
from matplotlib.animation import FuncAnimation

class Solution:
    def __init__(self, dimension, lower_bound, upper_bound, step, function, algorithm):
        self.d = dimension
        self.min = lower_bound
        self.max = upper_bound
        self.step = step
        self.f = function
        self.algorithm = algorithm
        self.params = list()
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig)
        self.init_params()
        self.tmp = []
        self.points = []


    def init_params(self):
        for i in range(self.d):
            self.params.append(np.arange(self.min, self.max, self.step))

        #print(self.params[0])
        self.params = np.meshgrid(*self.params)


    def print_graph(self):
        if self.d != 2:
            raise Exception("Function requires 2 dimensions.")

        x = self.params[0]
        y = self.params[1]
        z = self.f(self.params[:2])
        self.ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', alpha=0.7)

    def show_graph(self):
        if self.d != 2:
            raise Exception("Function requires 2 dimensions.")

        self.print_graph()
        plt.show()

    def find_minimum(self, aargs=()):
        self.tmp = self.algorithm(self.d, self.min, self.max, self.f, *aargs)
        return self.tmp[-1]

    def animate(self, i):
        if self.d != 2:
            raise Exception("Function requires 2 dimensions.")

        print("animating #" + str(i))

        for point in self.points:
            for x in point:
                x.remove()
        self.points = []

        for p in self.tmp[i]:
            self.points.append(self.ax.plot(p[0], p[1], self.f(p), 'ro'))

    def save_anim(self):
        if self.d != 2:
            raise Exception("Function requires 2 dimensions.")

        self.print_graph()
        anim = FuncAnimation(self.fig, self.animate, frames=len(self.tmp), interval=500)
        anim.save("{0}_{1}_{2}gen.gif".format(self.algorithm.__name__, self.f.__name__, len(self.tmp)), writer='pillow')





