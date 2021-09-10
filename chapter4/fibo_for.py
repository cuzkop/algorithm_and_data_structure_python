from util.measure_time import measure


def fibo(N):
    f = [0]*N
    f[0], f[1], f[2] = 0, 1, 1
    for n in range(3, N):
        f[n] = f[n-1] + f[n-2]

    return f[-1] + f[-2]

@measure
def call(N):
    return fibo(N)
    

print(call(7))