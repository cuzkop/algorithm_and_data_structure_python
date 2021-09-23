from util.measure_time import measure

# N = 4
# a = [3, 2, 6, 5]
# W = 14
a = [3, 2, 6, 5, 3, 5, 6, 1, 2, 8, 4, 1, 5, 2, 5, 2, 6, 7, 7, 2, 6, 8]
N = len(a)
W = 55

memo = []

def func(i, w, a):
    # print(i, w, a)
    if i == 0:
        return w == 0

    return func(i-1, w, a) or func(i-1, w-a[i-1], a)

@measure
def call(N, W, a):
    return func(N, W, a)

print(call(N, W, a))

