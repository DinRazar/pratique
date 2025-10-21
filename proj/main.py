from calculator.basic import add, subtract, multiply
from calculator.advanced import power, square_root

print(add(2, 3))             # Вывод: 5
print(subtract(5, 2))        # Вывод: 3
print(power(2, 3))           # Вывод: 8
print(square_root(16))       # Вывод: 4.0
print(multiply(4, 5))     

from calculator.advanced.exponentiation import power  
print(power(3, 4)) 

import sys
print(sys.path)

from calculator.advanced import sin, cos, tan
import math

print(sin(math.pi/2))     
print(cos(0))             
print(tan(math.pi/4))     