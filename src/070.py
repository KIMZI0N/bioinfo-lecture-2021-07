# ## 또는 #로 시작하지 않는 줄(data line)의 개수 세기.
cnt_all = 0
cnt_pass = 0

with open("070.vcf", "r") as handle:
    for line in handle:
        # ##먼저 if로 걸러야함. 순서 중요.
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)
