from util.measure_time import measure


def sum_func(N):
    if N == 0:
        return 0

    return N + sum_func(N-1)

@measure
def call(N):
    return sum_func(N)

print(call(3))