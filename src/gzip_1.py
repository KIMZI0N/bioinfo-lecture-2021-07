#! /usr/bin/env python

file_name = 'covid19.fasta'
data = dict() # data = {}
with open(file_name,'r') as handle:
    for line in handle:
        if line.startswith(">"): #헤더부분은 그냥 넘어감.
            continue
        for base in line.strip(): #\n 날리기.
            if base not in data: #base: A, G, C, T
                data[base] = 0 #base가 없으면 0
            data[base] += 1 #있으면 +1

print(data)
