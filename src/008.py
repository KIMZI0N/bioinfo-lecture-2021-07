#! /usr/bin/env python

import sys
n = int(sys.argv[1])
val = 1
while n > 0:
    val *= n
    n -= 1
print(val)

'''
fac = 1
i = 1

while i < 6:
    fac *= i
    i += 1

print(fac)
'''
