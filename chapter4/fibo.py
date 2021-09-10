from util.measure_time import measure


def fibo(N):
    if N == 0:
        return 0
    
    if N == 1:
        return 1

    return fibo(N-1) + fibo(N-2)

@measure
def call(N):
    return fibo(N)

print(call(6))
# 0 1 1 2 3 5 8 13 21