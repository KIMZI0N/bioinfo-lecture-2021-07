file_name = "rosalind_hamm.txt"
l = []
cnt = 0
with open(file_name, "r") as handle:
    for line in handle:
        l.append(line)
    for i in range(len(line)):
        if l[0][i] == l[1][i]:  # l에 비교할 2개의 string이 저장되어있음.
            continue
        else:
            cnt += 1
print(cnt)
