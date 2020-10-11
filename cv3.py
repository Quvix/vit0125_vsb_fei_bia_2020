from functions import *
from solution import Solution
from algorithms import *

s = Solution(2, -5.12, 5.12, 0.1, sphere, simulated_annealing)
print(s.find_minimum())
s.save_anim()
