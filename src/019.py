#! /usr/bin/env python
import sys

'''
with open('hahaha.txt','r') as handle:
    data = handle.readlines()

print(data)
#여기서 오류를 한 번 낸 후 어떤 오류인지 except다음에 쓰기
'''
try:
    with open('hahaha.txt','r') as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print(err)
#hahaha.txt를 생성하는 과정
    sys.exit()

print(data)
