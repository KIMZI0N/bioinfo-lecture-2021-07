#! /usr/bin/env python

seq = "AGTTTATAG"
#seq.index("TT")하면 2만 나옴.TTT가 연속되므로
for i in range(len(seq)):
    if seq[i:i+2] == 'TT':
        print(i)
    
