from util.measure_time import measure


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m%n)

@measure
def call(m, n):
    return gcd(m, n)

print(call(51, 15))