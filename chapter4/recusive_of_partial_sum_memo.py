from util.measure_time import measure
import random


a = [3, 2, 6, 5, 3, 5, 6, 1, 2, 8, 4, 1, 5, 2, 5, 2, 6, 7, 7, 2, 6, 8]
N = len(a)
W = 55

# W = random.randint(50, 100)
# a = [random.randint(2, 10) for _ in range(30)]
# N = len(a)

print(W, a)

memo = [[-1]*(W+1)]*(N+1)

def func(i, w, a):
    if i == 0:
        return w == 0

    # なぜかここがうまくいかないので土曜軽く話す
    if memo[i][w] != -1:
        return memo[i][w]


    if func(i-1, w, a):
        memo[i][w] = 1
        return memo[i][w]

    if func(i-1, w-a[i-1], a):
        memo[i][w] = 1
        return memo[i][w]

    memo[i][w] = 0

    return memo[i][w]

@measure
def call(N, W, a):
    return func(N, W, a)

print(call(N, W, a))

