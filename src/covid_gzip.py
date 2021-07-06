#! /usr/bin/env python

import gzip

file_name = 'covid19.fasta.gz'

data = dict() # data = {}

with gzip.open(file_name,'rt') as handle:
    for line in handle:
        if line.startswith(">"): #헤더부분은 그냥 넘어감.
            continue
        for base in line.strip(): #\n 날리기.
            if base not in data: #base: A, G, C, T
                data[base] = 0 #base가 없으면 0
            data[base] += 1 #있으면 +1

print(data)
