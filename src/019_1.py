#! /usr/bin/env python
import sys

try:
    num = int(input('enter: '))
except ValueError as err:
    print(err)
    sys.exit()
try:
    print( num  / 10)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
'''
#위의 두개를 하나로 묶는 방법
#어디서 에러가 났는지 모른다는 단점.
try:
    num = int(input('enter: '))
    print(10/num)
except ZeroDivisionError as err1:
    print(err1)
    sys.exit()
except ValueError as err2:
    print(err2)
    sys.exit()
'''
