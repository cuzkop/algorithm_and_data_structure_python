k = 2
n = 2

cnt = 0
for x in range(min(k, n)+1):
    for y in range(min(k, n)+1):
        z = n - x - y
        if 0 <= z <= k:
            cnt += 1


print(cnt)