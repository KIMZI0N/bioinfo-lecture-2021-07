#! /usr/bin/env python
data = [3, 1, 1, 2, 0, 0, 2, 3, 3]
print(min(data))
print(max(data))

cnt = dict()
for i in data:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
print(cnt)
