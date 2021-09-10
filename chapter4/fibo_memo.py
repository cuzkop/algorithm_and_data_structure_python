from util.measure_time import measure

memo = [-1]*50

def fibo(N):
    if N == 0 or N == 1:
        return N

    if memo[N] != -1:
        return memo[N]

    memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

@measure
def call(N):
    return fibo(N)

print(call(49))

for i in range(50):
    print(memo[i])