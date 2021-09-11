from util.measure_time import measure


def tribonacci(N):
    if N == 0 or N == 1:
        return 0

    if N == 2:
        return 1

    return tribonacci(N-1) + tribonacci(N-2) + tribonacci(N-3)

@measure
def call(N):
    return tribonacci(N)

print(call(7))
# 0 0 1 1 2 4 7 13 24 44