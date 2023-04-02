#In-built functions
# int() str() float() min() range() max() 



#module functions
import math
print(dir(math))

import random
print(dir(random))

import string
print(dir(string))

from math import sqrt
print(sqrt(4))

from math import*
print(sqrt(7))



#user-defined functions
def sum(a, b=4):
   print(a + b)

sum(1, 2)
sum(1)