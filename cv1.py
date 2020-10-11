from functions import *
from solution import Solution
from algorithms import *

s = Solution(2, -5.12, 5.12, 0.1, sphere, blind_search)
print(s.find_minimum(aargs=(100, 10)))
s.save_anim()



