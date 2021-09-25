n = 7
h = [2, 9, 4, 5, 1, 6, 10]
dp = [100]*n
dp[0] = 0
inf = 100

def chmin(res, b):
    if res > b:
        res = b

    return res

def rec(i):
    print(i, dp)
    if dp[i] < inf:
        return dp[i]

    if i == 0:
        return 0
    
    res = inf

    res = chmin(res, rec(i-1) + abs(h[i]-h[i-1]))

    if i > 1:
        res = chmin(res, rec(i-2) + abs(h[i]-h[i-2]))

    dp[i] = res
    return dp[i]

print(rec(n-1))