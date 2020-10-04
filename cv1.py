import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import math
from functions import *
from solution import Solution
from algorithms import *

#print(np.random.normal(0, 0.1, 100))

s = Solution(2, -5.12, 5.12, 0.1, sphere, blind_search)
print(s.find_minimum(100, 10))
s.save_anim()



