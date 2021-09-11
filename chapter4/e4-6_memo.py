import random
import time

W = random.randint(50, 500)
A = [random.randint(10, 30) for _ in range(20)]
N = len(A)

def rec(i, w, a, memo):
    if i == 0:
        return w == 0
    if i in memo and w in memo[i]:
        return memo[i][w]
    memo[i] = {w: rec(i-1, w, a, memo)}
    memo[i][w-a[i-1]] = rec(i-1, w-a[i-1], a, memo)
    return memo[i][w] or memo[i][w-a[i-1]]

def rec_not_memo(i, w, a):
    if i == 0:
        return w == 0

    return rec_not_memo(i-1, w, a) or rec_not_memo(i-1, w-a[i-1], a)

def main():
    print("memo start")
    t1 = time.time()
    print(rec(N, W, A, {}))
    t2 = time.time()
    print(f"memo end. time = {(t2 - t1):.4f}s")
    print("not memo start")
    t3 = time.time()
    print(rec_not_memo(N, W, A))
    t4 = time.time()
    print(f"not memo end. time = {(t4 - t3):.4f}s")

main()