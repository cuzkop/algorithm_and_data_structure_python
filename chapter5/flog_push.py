n = 7
h = [2, 9, 4, 5, 1, 6, 10]
dp = [100]*n
dp[0] = 0

def chmin(dp, i, b):
    print(dp[i], b)
    if dp[i] > b:
        dp[i] = b

for i in range(0, n):
    if i+1 < n:
        chmin(dp, i+1, dp[i] + abs(h[i]-h[i+1]))

    if i+2 < n:
        chmin(dp, i+2, dp[i] + abs(h[i]-h[i+2]))

print(dp)