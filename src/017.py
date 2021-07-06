#! /usr/bin/env python

file_name = "write_sample.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n")

with open(file_name, "a") as handle:
    handle.write("ken\n")

# csv를 tsv로 변환하기
s = "s1,s2,s3" #csv
data = s.split(",")
print(data) # ['s1', 's2', 's3']

#'a'는 append 파일에 내용 추가
with open(file_name, "a") as handle:
    handle.write("\t".join(data)+"\n")
