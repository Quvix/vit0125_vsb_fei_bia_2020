from functions import *
from solution import Solution
from algorithms import *

s = Solution(2, -5.12, 5.12, 0.1, sphere, hill_climbing)
print(s.find_minimum(100, 10))
s.save_anim()