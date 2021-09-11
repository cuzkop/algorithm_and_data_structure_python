from cmath import inf


N = 6
h = [30, 10, 60, 10, 60, 50]

# 配る遷移での実装

def chmin(l, i, v):
    if l[i] > v:
        l[i] = v


def flog():
    dp = [inf] * N
    dp[0] = 0

    for i in range(N):
        if i < N-1:
            chmin(dp, i+1, dp[i] + abs(h[i] - h[i+1]))
        if i < N-2:
            chmin(dp, i+2, dp[i] + abs(h[i] - h[i+2]))
    return dp

print(flog()[N-1])