N = 3
K = 10
a = [8, 5, 4]
b = [4, 1, 9]
inf = 1000

min_value = inf

for i in a:
    for j in b:
        if i + j < K:
            continue

        if i + j < min_value:
            min_value = i + j

print(min_value)