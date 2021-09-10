from util.measure_time import measure

N = 4
a = [3, 2, 6, 5]
W = 14



def func(i, w, a):
    print(i, w, a)
    if i == 0:
        return True if w == 0 else False

    return func(i-1, w, a) or func(i-1, w-a[i-1], a)

@measure
def call(N, W, a):
    return func(N, W, a)

print(call(N, W, a))