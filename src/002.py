#! /usr/bin/env python
#1
r = 3
pi = 3.141592
a = pi * r**2
print(a)

#2
import math
r = 2
print(math.pi*r**2)

#3
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()

r = int(sys.argv[1])
result = round(math.pi*r**2,2)
print(result)
