#! /usr/bin/env python
import sys

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [num]')
    sys.exit()

num = int(sys.argv[1])
#사진보고 수정하기.
if num % 3 == 0 and num % 7 == 0:
    print(f'{num}은 3과 7의 배수')
elif num % 3 == 0:
    print(f'{num}은 3의 배수')
elif num % 7 == 0:
    print(f'{num}은 7의 배수')

