file_name = "coPoMu.txt"
l = []
cnt = 0
with open(file_name, "r") as handle:
    for line in handle:
        l.append(line)
    for i in range(len(line)):
        if l[0][i] == l[1][i]:
            continue
        else:
            cnt += 1
print(cnt)
