#! /usr/bin/env python

s = input('input:')
if s.isalpha():
    print(f'{s}는 문자')
else: 
    print(type(s))
    print(f'{s}는 숫자')
