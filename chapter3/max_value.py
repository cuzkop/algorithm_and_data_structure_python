# N個の整数a0,a1,...,aN－1が与えられます．この中から２つ選んで差をとります．その差の最大値を求めるO(N)のアルゴリズムを設計してください．

n = 5
a = [8,3,200,100,9]

min_v = 1000
max_v = -1

for i in a:
    if i < min_v:
        min_v = i

    if i > max_v:
        max_v = i

print(max_v - min_v)
