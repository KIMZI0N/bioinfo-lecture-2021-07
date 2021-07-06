#! /usr/bin/env python

file_name = "read_sample.txt"
'''
#1
with open(file_name, 'r') as handle:
for line in handle:
print(line) #line에 이미 \n가 들어있음.
#print()도 디폴트end가 \n이므로 enter가 두번씩 쳐짐.
#print(line, end' ')하면 end를 띄어쓰기로 바꿀 수 있음.
#2
#print(line.strip()) #line의 \n를 없앨 수 있음.

#3
handle = open(file_name,'r')
for line in handle:
print(line.strip())
handle.close()

#with open 대신 그냥 open하면 반드시: close()해야하고 들여쓰기 안함.

#4
handle = open(file_name,'r')
lines = handle.readlines()
for line in lines:
    print(line.strip())
handle.close()
'''
#취향껏 용도에 맞게..
#5
with open(file_name, 'r') as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.strip())
