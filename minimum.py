# N(>=2)個の相異なる整数a0,a1,...,aN－1が与えられます．このうち２番目に小さい値を求めるO(N)のアルゴリズムを設計してください

n = 5
a = [8,3,200,100,9]

# min_value = 1000
# min2_value = 1000
min_v = 1000
min_v2 = 1000

for v in a:
    if min_v >= v:
        min_v2 = min_v
        min_v = v
    if min_v < v <= min_v2:
        min_v2 = v

print(min_v2)

# for i in a:
#     if i < min_value:
#         min2_value = min_value
#         min_value = i
#         continue

#     if min_value < i < min2_value:
#         min2_value = i

# print(min2_value)
