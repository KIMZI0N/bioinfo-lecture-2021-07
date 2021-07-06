#! /usr/bin/env python

class ValueCalculator:
    def __init__(self, val: str):
        self.val = val

    def __add__(self,other):
        return self.val + other.val
#이 파일을 import하면  print 안되고 이 파일을 직접 실행할 때만 print됨.
if __name__ == "__main__":
    print('hi')
