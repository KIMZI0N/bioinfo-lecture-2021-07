#! /usr/bin/env python

a ='Bio'
b ='Informatics'
c = a + b
print(c)

class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
    def __mul__(self, other):
        return '__mul__'

a1 = A('a')
a2 = A('b')
print(a1.val + a2.val)
print(a1 + a2)
print(a1 * a2)

#vcf는 변이를 담고 있는 파일
