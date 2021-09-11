# https://atcoder.jp/contests/dp/tasks/dp_a

from cmath import inf


N = 6
h = [30, 10, 60, 10, 60, 50]

# 自分の解
def rec(i: int, memo: dict[int, int]) -> int:
    if i == 0:
        return 0
    if i == 1:
        return abs(h[0] - h[1])
    if i in memo:
        cost = min(rec(i-1, memo) + abs(h[i] - h[i-1]), rec(i-2, memo) + abs(h[i] - h[i-2]))
        if memo[i] >= cost:
            memo[i] = cost
        return memo[i]
    else:
        memo[i] = min(rec(i-1, memo) + abs(h[i] - h[i-1]), rec(i-2, memo) + abs(h[i] - h[i-2]))
        return memo[i]
    
print(rec(N-1, {}))

def flog():
    dp = [inf] * N
    dp[0] = 0
    dp[1] = abs(h[0] - h[1])

    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))
    
    return dp[N-1]

print(flog())