n = 3
m = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    a,b,c = m[i-1]
    dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

print(max(dp[-1]))