#! /usr/bin/env python
seq = "ATGTTATAG"
'''
#1 if문
list=[]
for i in range(len(seq)):
    if seq[i] == 'A':
        list.append('T')
    elif seq[i] == 'T':
        list.append('A')
    elif seq[i] == 'G':
        list.append('C')
    elif seq[i] == 'C':
        list.append('G')
l = ''.join(list)
print(l)
'''
#2 강사님
comp_seq=""
comp_data = {"A":"T", "T":"A", "G":"C", "C":"G"}
for s in seq:
    comp_seq += comp_data[s]
print(seq)
print(comp_seq)

for i in range(len(seq)):
    s = seq[i]
    cs = comp_seq[i]
    bond = "≡"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{cs}")    

'''
#3 replace이용
Seq = s.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
print(Seq.upper())
'''
